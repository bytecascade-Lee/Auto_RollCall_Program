#!/usr/bin/env python3
# -*- coding:UTF-8 -*-
import logging
from configparser import ConfigParser
from csv import reader
from json import load
from os import startfile, system
from pathlib import Path
from re import findall
from .constant import *


temp: Path = Path(__file__).parent.parent  # 返回对象是一个 <class 'pathlib._local.WindowsPath'> 类，可以直接传递给open函数
# print(temp)  D:\python\点名

try:
    with open(file=temp / r'core.json', mode='r', encoding='utf-8') as file:
        CORE = load(file)
except FileNotFoundError:
    print('文件不存在: core.json')
    print('File does not exist: core.json')
    exit(-100001)


keys: List[String] = ['name', 'parameter', 'output', 'cache',
    'attendance', 'lang', 'config_setup',
    'function', 'constant', '__init__', 'readme']

文件路径, 文件编码 = [{}, {}]

for key in keys:
    文件路径[f"{key}"] = temp / CORE[key]['path']
    文件编码[f"{key}"] = CORE[key]['decode']
    if not Path.is_file(文件路径[f"{key}"]):
        err1: String = f'文件不存在: {CORE[key]['path']}'
        err2: String = f'File does not exist: {CORE[key]['path']}'
        print(err1); print(err2); logging.critical('0o00000x000')
        exit(-100002)

logging.basicConfig(
        level=logging.INFO,
        format='%(levelname)s:   Time=%(asctime)s\n\t\tFile=%(pathname)s, in lines %(lineno)d\n\t\tMessage=%(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        filename=文件路径['cache'],
        filemode='a+',
        encoding=文件编码['cache'])

logging.info('启动程序\n')

文本: ConfigParser = ConfigParser()
文本.read(filenames=文件路径['lang'], encoding=文件编码['lang'])

with open(file=文件路径['parameter'], mode='r', encoding=文件编码['parameter']) as file:
    parameter_user_get_error = True
    无重: Int = 1
    语音: Int = 1
    语言: String = '中文'
    用户参数: List[String] = findall(r'<([^>]+)>', file.read())
    try:
        无重: Int = int(用户参数[0])
        语音: Int = int(用户参数[1])
        语言: String = 用户参数[2]
    finally:
        pass

check = True # 初始化循环条件
while check:
    with open(file=文件路径['name'], mode='r', encoding=文件编码['name']) as file:
        总名单: Set[String] = {j for i in file.readlines() if (j := i.strip())}
        当前名单: Set[String] = 总名单.copy()
        check: Bool = not len(总名单) # 名单为空则返回true，继续循环；名单有内容则返回false，终止循环
        if check:
            m = 文本.get(语言, option='A.AK')
            print(m), logging.critical(m)
            startfile(文件路径['name'])
            system('pause')

with open(file=文件路径['attendance'], mode='r', encoding=文件编码['attendance']) as file:
    历史被点到: List[String] = [j for i in reader(file) if i for j in i[1:]]
