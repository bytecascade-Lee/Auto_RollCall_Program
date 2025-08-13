#!/usr/bin/env python3
# -*- coding:UTF-8 -*-
# 提交时间：2025年8月13日
# 版本号：4.3.1
from datetime import datetime
from io import TextIOWrapper

from package.config_setup import *


def 红色(content: Any) -> String:
    return RED + str(content) + RESET


def 蓝色(content: Any) -> String:
    return BLUE + str(content) + RESET


def 青色(content: Any) -> String:
    return CYAN + str(content) + RESET


def 绿色(content: Any) -> String:
    return GREEN + str(content) + RESET


def 黄色(content: Any) -> String:
    return YELLOW + str(content) + RESET


def 黑色(content: Any) -> String:
    return BLACK + str(content) + RESET


def 取整输入(*args):
    while True:
        print(*args, end='')
        sc = input()
        try:
            return int(sc)
        except Exception as e:
            if sc == 'exit':
                exit(-1)
            print(红色(e), 青色(sc))


def 功能打印(obj):
    def temp(index, content, color: Callable[Any, String]):
        print(' ', end='')
        print(color(index).rjust(2), end=' ')
        print(color(content))

    for _i, _j in obj.items():
        if _i in support:
            temp(_i, _j, 黄色)
    for _i, _j in obj.items():
        if _i not in support:
            temp(_i, _j, 黑色)


def text(content: Union[String, Collection[String]]) -> Union[String, List[String], None]:
    if isinstance(content, String):
        return 文本.get(语言, content.upper())
    if isinstance(content, Iterable):
        return [文本.get(语言, _i.upper()) for _i in content]
    return None


def space(times: Int=1):
    times = '\n' * times
    print(f"\n-------------------{times}".center(5))


def 格式化输出(obj: Union[List, Set, Tuple, Dict], file: Union[String, Path, TextIOWrapper, None]=None):
    length = len(obj)
    count = 0
    print(青色(length), 红色('BEGIN  ↓'), )
    for _i in obj:
        if (count + 1) % 7 == 0 or count == length - 1:
            end = '\n'
        else:
            end = ''
        print(青色(_i.ljust(5)), end=end, file=file)
        count += 1
    print(青色(length), 红色('END  ↑'), )


def support_ctrl(condition: Bool, mode: Literal['a', 'd'], *_z: Int):
    if condition:
        operations = {
            'd': lambda x, y: x.remove(y),
            'a': lambda x, y: x.add(y)}
        for _i in _z:
            operations[mode](support, _i)

def 当前时间() -> String:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
