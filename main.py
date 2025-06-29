#!/usr/bin/env python3
# -*- coding:UTF-8 -*-
# 提交时间：2025年6月28日23:15:21
# 版本号：4.2
from os import startfile
from csv import writer
from fractions import Fraction
from random import choice, seed
from shutil import copy2, rmtree
from time import time

from package.function import *

print(text('a.af'), 当前时间())
print(text('a.ag'), 用户参数)
print(text('a.ah'))
global 当前名单, 当前被点到
for i, j in zip((FUNC_main, FUNC_auxiliary, FUNC_check),
                (func_main, func_auxiliary, func_check)):
    for k, l in enumerate(j):
        i[int(l.split('.')[0])] = text(j)[k]
space()
while True:
    for i in range(13):
        support.add(i)
    support_condition = [[len(历史被点到) == 0,'d', (3, 5, 8)], [len(当前名单) == 0, 'd', (6,)],
                         [len(当前被点到) == 0, 'd', (7, 9)], [len(当前名单) != 0, 'a', (6,)]]
    for i in support_condition:
        support_ctrl(i[0], i[1], *i[2])
    print(support)
    功能打印(FUNC_main)
    x = 取整输入(绿色((text('a.ai'))))
    if not (x in range(0, 13)):
        print(text('0.01'))
    if not (x in support):
        功能打印(FUNC_check.get(x))

    if x == 1:
        while True:
            length = len(总名单) if 用户参数[0] == 0 else (len(总名单) - len(当前被点到))
            y = 取整输入(青色(length), 黄色(text('1.02')))
            if y <= 0:
                break
            本轮被点到 = []
            if y >= length:
                当前被点到 = set(当前名单) | 当前被点到
                历史被点到 += 当前名单; 本轮被点到 += 当前名单
                当前名单 = [i for i in 总名单]
                y -= length
            for i in range(y):
                seed(int(time() * 10 ** 3))
                cho = choice(当前名单)
                当前被点到.add(cho); 历史被点到.append(cho); 本轮被点到.append(cho)
                if 用户参数[0] == 1:
                    当前名单.remove(cho)
            with open(file=文件路径['attendance'], mode='a', encoding=文件编码['attendance'], newline='') as file:
                writer(file).writerow([当前时间()] + 本轮被点到)
            格式化输出(本轮被点到)
            if 语音:
                engine.say('。'.join(本轮被点到))
                engine.runAndWait()
            space()

    if x == 2:
        格式化输出(总名单)

    if x == 3:
        格式化输出(历史被点到)

    if x == 0:
        space(_x=2)
        while True:
            功能打印(FUNC_auxiliary)
            x = 取整输入(绿色(text('A.AI')))
            if x == 0:
                break

            if x == 4:
                print(input() in 总名单)

            if x == 5:
                copy2(文件路径['attendance'], temp / rf'\user\history\{当前时间()}.csv')
                with open(file=文件路径['attendance'], mode='w', encoding=文件编码['attendance']) as file:
                    pass
                已被点到, 本轮被点到 = [[], []]
                logging.info(text('A.AD'))
                print(黄色(text('5.02')))

            if x == 6:
                比对名单 = {i for i in 总名单 if not (i in 当前被点到)}
                格式化输出(比对名单)

            if x == 7:
                with open(file=文件路径['output'], mode='a', encoding=文件编码['output']) as file:
                    print(text('7.02'), 当前时间(), file=file)
                    格式化输出(当前被点到, file=file)
                    file.write('\n\n')
                logging.info(text('a.ae'))
                print(黄色(text('7.03')), 青色(文件路径['output']))

            if x == 8:
                while True:
                    y = [s for s in input(绿色(text('8.02'))).split('/')]
                    if y[0] == '0':
                        break
                    print(黄色(text('8.03').center(6)))
                    概率 = Fraction(1, len(总名单))
                    for i in y:
                        次数 = 历史被点到.count(i)
                        频率 = Fraction(次数, len(历史被点到))
                        if i in 总名单:
                            print(f'{蓝色(i)} | {青色(次数)} | {青色(频率)} | {青色(概率)}')
                        elif 次数:
                            print(f'{蓝色(i)} | {青色(次数)} | {青色(频率)} | {红色(text('8.04'))}')
                        else:
                            print(青色(i), 红色(text('8.05')))
                    space()

            if x == 9:
                格式化输出(当前被点到)
                print(黄色(text('9.02')), 青色(len(当前被点到)))

            if x == 10:
                print(FUNC_elemnt)
                y = 取整输入(绿色(text('10.03')))
                if y not in [1, 2]:
                    continue
                成员 = {s for s in input(绿色(text('10.04'))).split('/') if s}
                if not 成员:
                    continue
                添加成员, 删除成员 = [[], []]
                if y == 1:
                    成员 = [i for i in 成员 if i not in 总名单]
                    总名单.update(成员), 当前名单.extend(成员), 添加成员.extend(成员)
                    with open(file=文件路径['name'], mode='a', encoding=文件编码['name']) as file:
                        file.writelines(总名单)
                    print(黄色(text('10.05')), 青色(','.join(添加成员)))
                if y == 2:
                    成员 = [i for i in 成员 if i in 总名单]
                    for i in 成员:
                        总名单.remove(i); 当前名单.remove(i); 删除成员.append(i)
                    with open(file=文件路径['name'], mode='w', encoding=文件编码['name']) as file:
                        file.writelines(总名单)
                    print(黄色(text('10.06')), 青色(','.join(删除成员)))
                格式化输出(当前名单)

            if x == 11:
                print(蓝色(text('11.02')))
                startfile(文件路径['parameter'])

            if x == 12:
                with open(file=文件路径['cache'], mode='w', encoding=文件编码['cache']) as file:
                    pass
                rmtree(r'user\history', ignore_errors=True)
            space()
    space()
