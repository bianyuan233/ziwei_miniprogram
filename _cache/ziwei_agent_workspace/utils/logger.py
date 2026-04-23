import os
import logging
import traceback
from datetime import datetime
from logging.handlers import RotatingFileHandler

class UnifiedLogger:
    """统一日志模块，同时输出到控制台和文件"""

    _instances = {}  # 按 name 缓存 logger 实例

    def __init__(self, name: str, log_dir: str = None):
        self.name = name
        self.log_dir = log_dir or os.path.join(os.path.dirname(__file__), "..", "logs")
        os.makedirs(self.log_dir, exist_ok=True)

        # 创建 logger
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        self.logger.handlers = []  # 清空已有 handlers，避免重复

        # 控制台 handler (INFO 级别)
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        console_formatter = logging.Formatter(
            '[%(asctime)s] %(name)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        ch.setFormatter(console_formatter)

        # 文件 handler (DEBUG 级别，使用 RotatingFileHandler)
        log_file = os.path.join(self.log_dir, f"{name}.log")
        fh = RotatingFileHandler(
            log_file, maxBytes=10*1024*1024, backupCount=5, encoding="utf-8"
        )
        fh.setLevel(logging.DEBUG)
        file_formatter = logging.Formatter(
            '[%(asctime)s] %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        fh.setFormatter(file_formatter)

        self.logger.addHandler(ch)
        self.logger.addHandler(fh)

    def debug(self, msg): self.logger.debug(msg)
    def info(self, msg): self.logger.info(msg)
    def warning(self, msg): self.logger.warning(msg)
    def error(self, msg, exc_info=False):
        if exc_info:
            self.logger.error(f"{msg}\n{traceback.format_exc()}")
        else:
            self.logger.error(msg)
    def critical(self, msg, exc_info=False):
        if exc_info:
            self.logger.critical(f"{msg}\n{traceback.format_exc()}")
        else:
            self.logger.critical(msg)


# 全局日志实例
_app_logger = None
_agent_logger = None
_global_logger = None


def get_app_logger(log_dir: str = None) -> UnifiedLogger:
    """获取 app.py 使用的日志实例"""
    global _app_logger
    if _app_logger is None:
        _app_logger = UnifiedLogger("app", log_dir)
    return _app_logger


def get_agent_logger(log_dir: str = None) -> UnifiedLogger:
    """获取 agent.py 使用的日志实例"""
    global _agent_logger
    if _agent_logger is None:
        _agent_logger = UnifiedLogger("agent", log_dir)
    return _agent_logger


def get_global_logger(log_dir: str = None) -> UnifiedLogger:
    """获取全局日志实例（记录启动、异常等）"""
    global _global_logger
    if _global_logger is None:
        _global_logger = UnifiedLogger("global", log_dir)
    return _global_logger


def log_to_session(log_dir: str, session_id: str, level: str, msg: str):
    """按会话ID记录日志到单独文件

    Args:
        log_dir: 日志根目录
        session_id: 会话ID
        level: 日志级别 debug/info/warning/error
        msg: 日志消息
    """
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(log_dir, f"{session_id}.log")

    # 同时写入会话专属文件和全局 instance 文件
    with open(log_file, 'a', encoding="utf-8") as f:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        f.write(f"[{timestamp}] {level.upper()} - {msg}\n")

    # 也写入 instance 日志
    logger = get_global_logger(log_dir)
    getattr(logger, level)(f"[{session_id}] {msg}")
