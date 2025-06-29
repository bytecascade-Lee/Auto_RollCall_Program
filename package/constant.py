#!/usr/bin/env python3
# -*- coding:UTF-8 -*-
# 提交时间：2025年6月28日23:15:26
# 版本号：4.2
import pyttsx3
import colorama


colorama.init(autoreset=True)

BLUE = colorama.Fore.LIGHTBLUE_EX # 提示，说明
CYAN = colorama.Fore.LIGHTCYAN_EX # 姓名，数字
GREEN = colorama.Fore.LIGHTGREEN_EX # 输入
YELLOW = colorama.Fore.LIGHTYELLOW_EX # 操作，输出
RED = colorama.Fore.LIGHTRED_EX # 错误
BLACK = colorama.Fore.LIGHTBLACK_EX # 操作
RESET = colorama.Style.RESET_ALL # 恢复

engine = pyttsx3.init()
engine.setProperty(name='rate', value=200)
engine.setProperty(name='volume', value=1.0)

func_main = ['0.00', '1.00', '2.00', '3.00']
func_auxiliary = ['4.00', '5.00', '6.00', '7.00', '8.00', '9.00', '10.00', '11.00', '12.00']
func_check = ['0.01', '4.01', '5.01', '6.01', '7.01', '8.01', '9.01']
func_elemnt = ['10.02.00', '10.02.01']

FUNC_main, FUNC_auxiliary, FUNC_check, FUNC_elemnt = [{}, {}, {}, {}]

support = set({})

当前被点到 = set({})
