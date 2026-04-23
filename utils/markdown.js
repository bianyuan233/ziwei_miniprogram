function textNode(text) {
  return {
    type: 'text',
    text: String(text || '')
  };
}

function element(name, attrs, children) {
  return {
    name,
    attrs: attrs || {},
    children: children || []
  };
}

function renderInline(text) {
  const source = String(text || '');
  const nodes = [];
  const pattern = /(\*\*[^*]+\*\*|`[^`]+`|\[[^\]]+\]\([^)]+\))/g;
  let lastIndex = 0;
  let match;

  while ((match = pattern.exec(source)) !== null) {
    if (match.index > lastIndex) {
      nodes.push(textNode(source.slice(lastIndex, match.index)));
    }

    const token = match[0];
    if (token.startsWith('**')) {
      nodes.push(element('strong', null, [textNode(token.slice(2, -2))]));
    } else if (token.startsWith('`')) {
      nodes.push(element('code', { class: 'md-inline-code' }, [textNode(token.slice(1, -1))]));
    } else {
      const linkMatch = token.match(/^\[([^\]]+)\]\(([^)]+)\)$/);
      if (linkMatch) {
        nodes.push(element('span', { class: 'md-link' }, [textNode(linkMatch[1])]));
      } else {
        nodes.push(textNode(token));
      }
    }

    lastIndex = pattern.lastIndex;
  }

  if (lastIndex < source.length) {
    nodes.push(textNode(source.slice(lastIndex)));
  }

  return nodes.length ? nodes : [textNode(source)];
}

function flushParagraph(nodes, lines) {
  if (!lines.length) return;
  nodes.push(element('p', { class: 'md-p' }, renderInline(lines.join('\n'))));
  lines.length = 0;
}

function flushList(nodes, listItems) {
  if (!listItems.length) return;
  nodes.push(element('ul', { class: 'md-list' }, listItems.map(item =>
    element('li', { class: 'md-list-item' }, renderInline(item))
  )));
  listItems.length = 0;
}

function markdownToNodes(markdown) {
  const nodes = [];
  const paragraph = [];
  const listItems = [];
  const lines = String(markdown || '').replace(/\r\n/g, '\n').split('\n');
  let inCode = false;
  let codeLines = [];

  lines.forEach(line => {
    if (/^```/.test(line.trim())) {
      if (inCode) {
        nodes.push(element('pre', { class: 'md-code-block' }, [textNode(codeLines.join('\n'))]));
        codeLines = [];
        inCode = false;
      } else {
        flushParagraph(nodes, paragraph);
        flushList(nodes, listItems);
        inCode = true;
      }
      return;
    }

    if (inCode) {
      codeLines.push(line);
      return;
    }

    if (!line.trim()) {
      flushParagraph(nodes, paragraph);
      flushList(nodes, listItems);
      return;
    }

    const headingMatch = line.match(/^(#{1,3})\s+(.+)$/);
    if (headingMatch) {
      flushParagraph(nodes, paragraph);
      flushList(nodes, listItems);
      nodes.push(element('h' + headingMatch[1].length, { class: 'md-heading' }, renderInline(headingMatch[2])));
      return;
    }

    const listMatch = line.match(/^\s*(?:[-*+]|\d+\.)\s+(.+)$/);
    if (listMatch) {
      flushParagraph(nodes, paragraph);
      listItems.push(listMatch[1]);
      return;
    }

    if (/^>\s+/.test(line)) {
      flushParagraph(nodes, paragraph);
      flushList(nodes, listItems);
      nodes.push(element('blockquote', { class: 'md-quote' }, renderInline(line.replace(/^>\s+/, ''))));
      return;
    }

    flushList(nodes, listItems);
    paragraph.push(line);
  });

  if (inCode) {
    nodes.push(element('pre', { class: 'md-code-block' }, [textNode(codeLines.join('\n'))]));
  }
  flushParagraph(nodes, paragraph);
  flushList(nodes, listItems);

  return nodes.length ? nodes : [element('p', { class: 'md-p' }, [textNode('')])];
}

module.exports = {
  markdownToNodes
};
