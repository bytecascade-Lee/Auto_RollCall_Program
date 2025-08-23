#!/usr/bin/env python3
# -*- coding:UTF-8 -*-
# 提交时间：2025年8月13日
# 版本号：4.3.1
import pyttsx3
import colorama
from typing import *

String: TypeAlias = str
Int: TypeAlias = int
Float: TypeAlias = float
Bool: TypeAlias = bool
ColoramaColor: TypeAlias = str

colorama.init(autoreset=True)

BLUE: ColoramaColor = colorama.Fore.LIGHTBLUE_EX # 提示，说明
CYAN: ColoramaColor = colorama.Fore.LIGHTCYAN_EX # 姓名，数字
GREEN: ColoramaColor = colorama.Fore.LIGHTGREEN_EX # 输入
YELLOW: ColoramaColor = colorama.Fore.LIGHTYELLOW_EX # 操作，输出
RED: ColoramaColor = colorama.Fore.LIGHTRED_EX # 错误
BLACK: ColoramaColor = colorama.Fore.LIGHTBLACK_EX # 操作
RESET: ColoramaColor = colorama.Style.RESET_ALL # 恢复

engine = pyttsx3.init()
engine.setProperty(name='rate', value=200)
engine.setProperty(name='volume', value=1.0)

func_main: List[String] = ['1.00', '2.00', '3.00', '0.00']
func_auxiliary: List[String] = ['4.00', '5.00', '6.00', '7.00', '8.00', '9.00', '10.00', '11.00', '12.00']
func_check: List[String] = ['0.01', '3.01', '5.01', '6.01', '7.01', '8.01', '9.01']
func_dev: List[String] = ['10.02.01', '10.02.02']

FUNC_main, FUNC_auxiliary, FUNC_check, FUNC_dev = [{}, {}, {}, {}]

support = set({})
当前被点到 = []

添加成员, 删除成员 = [[], []]
dev_map: Dict[Int, Tuple[String, List]] = {1: ('10.05', 添加成员), 2: ('10.06', 删除成员)}
