import json
from datetime import datetime
from typing import Literal

from ziwei_const import *


class Person:

    def __init__(self, ziwei_json):
        self.ziwei_json = ziwei_json
        self.extract_format_info()

    # ! >>> 提取基本信息 >>>
    def extract_format_info(self):
        self.info = self.extract_info()
        self.basic_palaces = self.extract_basic_palaces()
        self.range_palaces = self.extract_range_palaces()
        self.age_palaces = self.extract_age_palaces()


    def extract_info(self):
        used_dct = self.ziwei_json['bySolar']
        info_dct = {}
        info_dct['性别'] = used_dct['gender']
        info_dct['出生日期（阳历）'] = used_dct['solarDate']
        info_dct[
            '出生日期（阴历）'] = f"{used_dct['rawDates']['lunarDate']['lunarYear']}-{str(used_dct['rawDates']['lunarDate']['lunarMonth']).zfill(2)}-{str(used_dct['rawDates']['lunarDate']['lunarDay']).zfill(2)}"
        info_dct['八字'] = used_dct['chineseDate']
        info_dct['生肖'] = used_dct['zodiac']
        return info_dct

    def extract_basic_palaces(self):
        used_lst = self.ziwei_json['bySolar']['palaces']
        basic_palaces_lst = [{
            'index': palaces['index'],
            'name': palaces['name'],
            '干支': palaces['heavenlyStem']+palaces['earthlyBranch'],
            '主星': [{'name': major_star['name'], 'brightness': major_star['brightness'], 'mutagen': major_star['mutagen']} for major_star in palaces['majorStars']],
            '辅星': [{'name': minor_star['name'], 'brightness': minor_star['brightness'], 'mutagen': minor_star['mutagen'] if 'mutagen' in minor_star else ''} for minor_star in palaces['minorStars']],
            '杂曜': [{'name': adjective_star['name'].strip()} for adjective_star in palaces['adjectiveStars']]
        } for palaces in used_lst]
        return basic_palaces_lst

    def extract_range_palaces(self):
        used_lst = self.ziwei_json['majorPeriods']
        range_palaces_lst = []
        for period in used_lst:
            ages = list(range(period['range'][0], period['range'][1] + 1))
            years = [age + self.ziwei_json['bySolar']['rawDates']['lunarDate']['lunarYear'] for age in range(period['range'][0], period['range'][1] + 1)]
            palaces = []
            for basic_palace, range_palace in zip(self.basic_palaces, period['palaces']):
                palaces.append({
                    'index':basic_palace['index'], 
                    'name': range_palace['name'], 
                    '干支':basic_palace['干支'], 
                    '主星':basic_palace['主星'],
                    '辅星':basic_palace['辅星'],
                    '杂曜':basic_palace['杂曜']
                })
            range_palaces_lst.append({'ages':ages,'years':years,'palaces':palaces})
        return range_palaces_lst

    def extract_age_palaces(self):
        used_lst = self.ziwei_json['yearlyPeriods']
        age_palaces_lst = []
        for period in used_lst:
            ages = [age for age in range(period['age'], period['age'] + 12*10 + 1, 12)]
            years = [age - 1 + self.ziwei_json['bySolar']['rawDates']['lunarDate']['lunarYear'] for age in range(period['age'], period['age'] + 12*10 + 1, 12)]
            palaces = []
            for basic_palace, age_palace in zip(self.basic_palaces, period['palaces']):
                palaces.append({
                    'index':basic_palace['index'], 
                    'name': age_palace['name'], 
                    '干支':basic_palace['干支'], 
                    '主星':basic_palace['主星'],
                    '辅星':basic_palace['辅星'],
                    '杂曜':basic_palace['杂曜']
                })
            age_palaces_lst.append({'ages':ages,'years':years,'palaces':palaces})
        return age_palaces_lst
    # ! <<< 提取基本信息 <<<

    # ! >>> 描述信息 >>>
    def describe_info(self):
        return str(self.info)

    def describe_palaces(self, mode: Literal["basic", "range", "age"]):
        return str(self.basic_palaces)
    # ! <<< 描述信息 <<<

    # ! >>> 规则原子函数 >>>
    def get_hua(self, sky, hua):
        """获取某个天干的某个化是哪个星

        Args:
            sky (str): 天干，如"甲"
            hua (str): 四化，如"科"

        Returns:
            str: 化的那颗星，如"紫薇"
        """        
        return SKYHUA[sky][hua]

    
    def get_palace_lst(self, palace_mode, year=None, age=None):
        """根据使用的命盘维度（本命、大限、流年）和年龄或者年份获取使用的是哪个盘

        Args:
            palace_mode (str): 本命、大限或流年
            year (int, optional): 定位的年份. Defaults to None.
            age (int, optional): 定位的年龄. Defaults to None.

        Returns:
            List: 对应维度和时间的命盘各宫信息
        """        
        palace_lst = []
        if palace_mode == DIMENSION_BASIC:
            palace_lst = self.basic_palaces
        elif palace_mode == DIMENSION_RANGE or palace_mode == DIMENSION_AGE:
            used_palace_lst_lst = []
            if palace_mode == DIMENSION_RANGE:
                used_palace_lst_lst = self.range_palaces
            elif palace_mode == DIMENSION_AGE:
                used_palace_lst_lst = self.age_palaces
            if year:
                for used_palace_lst in used_palace_lst_lst:
                    if year in used_palace_lst['years']:
                        palace_lst = used_palace_lst['palaces']
            elif age:
                for used_palace_lst in used_palace_lst_lst:
                    if age in used_palace_lst['ages']:
                        palace_lst = used_palace_lst['palaces']
        return palace_lst

    def get_opposite_palace(self, palace, palace_mode, year=None, age=None):
        """借宫，即获取某个维度某个宫的对宫，当两个宫中正好有一个宫没有主星时才能借宫，否则返回空字符串

        Args:
            palace (str): 宫名
            palace_mode (str): 本命、大限或流年
            year (int, optional): 定位的年份. Defaults to None.
            age (int, optional): 定位的年龄. Defaults to None.

        Returns:
            str: 当满足借宫规则时返回对应的宫名称，当不满足时返回空字符串
        """        
        index = 0
        opposite_palace = ''
        empty_count = 0
        used_palace_lst = self.get_palace_lst(palace_mode, year=year, age=age)
        for palace_item in used_palace_lst:
            if palace == palace_item['name']:
                index = palace_item['index']
                if len(palace_item['主星']) == 0:
                    empty_count += 1
                break
        opposite_index = (index + 6) % 12
        for palace_item in used_palace_lst:
            if palace_item['index'] == opposite_index:
                opposite_palace = palace_item['name']
                if len(palace_item['主星']) == 0:
                    empty_count += 1
                break
        if empty_count == 1:
            return opposite_palace
        else:
            return ''

    def palace_hua_palace(self, palace_0, palace_mode_0, palace_1, palace_mode_1, hua, year=None, age=None):
        """(本命、大限、流年)的某个宫是否天干化(权、禄、科、忌)到(本命、大限、流年)的某个宫

        Args:
            palace_0 (str): 起始宫名
            palace_mode_0 (str): 起始维度
            palace_1 (str): 化到宫名
            palace_mode_1 (str): 化到维度
            hua (str): 权、禄、科、忌
            year (int, optional): 定位的年份. Defaults to None.
            age (int, optional): 定位的年龄. Defaults to None.

        Returns:
            bool: 是否化到
        """        
        # 判断palace_0的天干hua是否在palace_1，当palace_mode_0或者palace_mode_1不为ZIWEI_BASIC时，需要看year或age来确定要拿哪个流年或大限的宫的数据
        # 第一步：找到0对应的天干然后找到化的那个星，记为hua_star
        sky_0 = ''
        used_palace_lst_0 = self.get_palace_lst(palace_mode_0, year, age)
        for palace in used_palace_lst_0:
            if palace['name'] == palace_0:
                sky_0 = palace['干支'][0]
                break
        if sky_0 == '':
            return False
        hua_star = self.get_hua(sky_0, hua)

        # 第二步，找到1对应的宫看有没有hua_star
        used_palace_lst_1 = self.get_palace_lst(palace_mode_1, year, age)
        for palace_item in used_palace_lst_1:
            if palace_1 == palace_item['name']:
                for star in palace_item['主星'] + palace_item['辅星']:
                    if hua_star == star['name']:
                        return True
        return False        

    def palace_hua(self, palace, palace_mode, hua, year=None, age=None):
        """判断某维度的某宫是否有某个化

        Args:
            palace (str): 宫名
            palace_mode (str): 本命、大限或流年
            hua (str): 四化，权、禄、科、忌
            year (int, optional): 定位年份. Defaults to None.
            age (int, optional): 定位年龄. Defaults to None.

        Returns:
            bool: 某维度某宫是否有某个四化
        """        
        # 判断某宫是否有某个四化
        used_palace_lst = self.get_palace_lst(palace_mode, year, age)
        for palace_item in used_palace_lst:
            if palace_item['name'] == palace:
                for star in palace_item['主星'] + palace_item['辅星']:
                    if hua == star['mutagen']:
                        return True
        return False


    # 本命大限流年的某个宫是否有某个星
    def palace_have_star(self, palace, palace_mode, star, borrow=False, year=None, age=None):
        """判断某个维度的某宫是否有某星

        Args:
            palace (str): 宫名
            palace_mode (str): 维度，本命、大限、流年
            star (str): 星名
            borrow (bool, optional): 是否要考虑借宫. Defaults to False.
            year (int, optional): 定位年份. Defaults to None.
            age (int, optional): 定位年龄. Defaults to None.

        Returns:
            bool: 是否有某星
        """        
        used_palace_lst = self.get_palace_lst(palace_mode, year, age)
        opposite_palace = ''
        if borrow:
            opposite_palace = self.get_opposite_palace(palace, palace_mode, year, age)
        for palace_item in used_palace_lst:
            if palace_item['name'] == palace or palace_item['name'] == opposite_palace:
                for star_item in palace_item['主星'] + palace_item['辅星'] + palace_item['杂曜']:
                    if star == star_item['name']:
                        return True
        return False


    # ! <<< 规则原子函数 <<<

    # ! >>> 内置函数 >>>
    def __str__(self):
        info_str = f'基本信息: \n{json.dumps(self.info, ensure_ascii=False, indent=2, separators=(',', ': '))}\n\n本命盘: \n{json.dumps(self.basic_palaces, ensure_ascii=False, indent=2, separators=(',', ': '))}\n\n大运盘: \n{json.dumps(self.range_palaces, ensure_ascii=False, indent=2, separators=(',', ': '))}\n\n流年盘: \n{json.dumps(self.age_palaces, ensure_ascii=False, indent=2, separators=(',', ': '))}'
        return info_str
    # ! <<< 内置函数 <<<
