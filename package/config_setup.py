#!/usr/bin/env python3
# -*- coding:UTF-8 -*-
# 提交时间：2025年6月28日23:15:32
# 版本号：4.2
import logging
from configparser import ConfigParser
from csv import reader
from json import load
from os import system
from pathlib import Path
from re import findall

temp = Path(__file__).parent.parent  # 返回对象是一个 <class 'pathlib._local.WindowsPath'> 类，可以直接传递给open函数
# print(temp)  D:\Mine_PyCodeLib\main点名\4.0及以上

try:
    with open(file=temp / r'core.json', mode='r', encoding='utf-8') as file:
        CORE = load(file)
except Exception as e:
    print(e)
    system('pause')


keys = [
    'name',
    'parameter',
    'output',
    'cache',
    'attendance',
    'lang',
    'config_setup',
    'function',
    'constant',
    '__init__',
    'readme'
]

文件路径 = {}
文件编码 = {}

# 循环处理每个键
for key in keys:
    文件路径[f"{key}"] = temp / CORE[key]['path']
    文件编码[f"{key}"] = CORE[key]['decode']

del CORE, key, keys

logging.basicConfig(
        level=logging.INFO,
        format='%(levelname)s:   Time=%(asctime)s\n\t\tFile=%(pathname)s, in lines %(lineno)d\n\t\tMessage=%(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        filename=文件路径['cache'],
        filemode='a+',
        encoding=文件编码['cache'])

logging.info('启动程序\n')


文本 = ConfigParser()
文本.read(filenames=文件路径['lang'], encoding=文件编码['lang'])

with open(file=文件路径['parameter'], mode='r', encoding=文件编码['parameter']) as file:
    try:
        用户参数 = findall(r'<([^>]+)>', file.read())
        无重: int = int(用户参数[0])
        语音: int = int(用户参数[1])
        语言: str = 用户参数[2]
    except Exception:
        parameter_user_get_error = True
        无重: int = 1
        语音: int = 1
        语言: str = '中文'

with open(file=文件路径['name'], mode='r', encoding=文件编码['name']) as file:
    总名单: set = {i.strip() for i in file.readlines() if i.strip()}
    当前名单: list = [i for i in 总名单]

if len(总名单) == 0:
    m = 文本.get(语言, 'A.AK')
    print(m), logging.critical(m)

with open(file=文件路径['attendance'], mode='r', encoding=文件编码['attendance']) as file:
    历史被点到: list = [j for i in reader(file) if i for j in i[1:]]
