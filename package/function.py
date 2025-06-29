#!/usr/bin/env python3
# -*- coding:UTF-8 -*-
# 提交时间：2025年6月28日23:15:35
# 版本号：4.2
from datetime import datetime
from package.constant import *
from package.config_setup import *


def 红色(_x):
    return RED + str(_x) + RESET


def 蓝色(_x):
    return BLUE + str(_x) + RESET


def 青色(_x):
    return CYAN + str(_x) + RESET


def 绿色(_x):
    return GREEN + str(_x) + RESET


def 黄色(_x):
    return YELLOW + str(_x) + RESET


def 黑色(_x):
    return BLACK + str(_x) + RESET


def 取整输入(*args):
    while True:
        print(*args, end='')
        _a = input()
        try:
            return int(_a)
        except Exception as e:
            if _a == 'exit':
                exit(-1)
            print(红色(e))


def 功能打印(_x):
    def temp(_a, _b, _c):
        print(' ', end='')
        print(_c(_a).rjust(2), end=' ')
        print(_c(_b))

    for _i, _j in _x.items():
        if _i in support:
            temp(_i, _j, 黄色)
    for _i, _j in _x.items():
        if _i not in support:
            temp(_i, _j, 黑色)


def text(_x):
    if isinstance(_x, str):
        return 文本.get(语言, _x.upper())
    if isinstance(_x, list):
        return [文本.get(语言, _i.upper()) for _i in _x]
    return None


def space(_x=1):
    _a = '\n' * _x
    print(f"\n-------------------{_a}".center(5))


def 格式化输出(_x, file=None):
    print(青色(len(_x)), '↓')
    _a = 0
    for _i in _x:
        if (_a + 1) % 7:
            _b = ''
        else:
            _b = '\n'
        print(青色(_i.ljust(5)), end=_b, file=file)
        _a += 1
    print(青色(len(_x)), '↑')


def support_ctrl(_x: bool, _y: str, *_z: int):
    if _x:
        for _k, _j in zip(range(len(_z)), _z):
            if _y == 'd':
                support.remove(_j)
            if _y == 'a':
                support.add(_j)


def 当前时间():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
