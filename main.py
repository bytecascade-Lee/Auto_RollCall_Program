#!/usr/bin/env python3
# -*- coding:UTF-8 -*-
from csv import writer
from random import choice, seed
from shutil import copy2, rmtree
from time import sleep, time

from package.function import *

print(text('a.af'), 青色(当前时间()))
print(text('a.ag'), 青色(用户参数))
print(红色(text('a.ah')))
global 当前名单, 当前被点到
for i, j, k in zip((FUNC_main, FUNC_auxiliary, FUNC_check, FUNC_dev),
                (func_main, func_auxiliary, func_check, func_dev),
                (0, 0, 0, 2)):
    for m in j:
        i[int(m.split('.')[k])] = text(m)
space()
logging.info(f'FUNC_check={FUNC_check}\n\t\t\tFUNC_dev={FUNC_dev}\n'
             f'\t\t\tFUNC_main={FUNC_main}\n\t\t\tFUNC_auxiliary={FUNC_auxiliary}')
while True:
    for i in range(13):
        support.add(i)
    support_condition = [[len(历史被点到) == 0,'d', (3, 5, 8)], [len(当前名单) == 0, 'd', (6,)],
                         [len(当前被点到) == 0, 'd', (7, 9)], [len(当前名单) != 0, 'a', (6,)]]
    for i in support_condition:
        support_ctrl(i[0], i[1], *i[2])
    logging.info(f'support= {support}')
    功能打印(FUNC_main)
    x = 取整输入(绿色((text('a.ai'))))
    if not (x in range(0, 4)):
        print(红色(text('0.01')), 青色(x))
        continue
    if not x in support:
        print(红色((temp:= FUNC_check.get(x))))
        logging.warning(temp)
        continue

    if x == 1:
        while True:
            length = len(总名单) if 用户参数[0] == 0 else (len(总名单) - len(当前被点到))
            y = 取整输入(f'{青色(length)}{黄色(text('1.02'))}')
            if y == 0:
                break
            暂缓区: Dict[Int, String] = {}
            if (y < 0) or ((y >= length) and 无重):
                print(text('1.01'))
            for i in range(y):
                seed(str(time()).split('.')[1])
                cho = choice(list(当前名单))
                暂缓区[i] = cho
                if 无重:
                    当前名单.remove(cho)
            temp = list(暂缓区.values())
            当前被点到.extend(temp)
            历史被点到.extend(temp)
            本轮被点到: tuple[String, Dict] = (当前时间(), 暂缓区)
            with open(file=文件路径['attendance'], mode='a', encoding=文件编码['attendance'], newline='') as file:
                writer(file).writerow([当前时间()] + (temp2:= list((temp:= 本轮被点到[1]).values())))
            格式化输出(temp)
            if 语音:
                engine.say('。'.join(temp2))
                engine.runAndWait()
            logging.info(f'1: {temp}')
            space()

    if x == 2:
        格式化输出(总名单)
        logging.info('2')

    if x == 3:
        格式化输出(历史被点到)
        logging.info('3')

    if x == 0:
        space(times=2)
        while True:
            功能打印(FUNC_auxiliary)
            x = 取整输入(绿色(text('A.AI')))
            if x == 0:
                break
            if not (x in range(4, 13)):
                print(红色(text("0.01")), 青色(x))
                continue
            if not x in support:
                print(红色((temp:= FUNC_check.get(x))))
                logging.warning(temp)
                continue
            

            if x == 4:
                y = 姓名输入(绿色(text('4.02')))
                for i in y:
                    condition = 绿色(text('4.03')) if i in 总名单 else 红色(text('4.04'))
                    print(蓝色(i), condition)
                logging.info('4')

            if x == 5:
                destination = PATH / rf'user\history\{当前时间()}.csv'
                destination.parent.mkdir(parents=True, exist_ok=True)
                copy2(文件路径['attendance'], destination)
                with open(file=文件路径['attendance'], mode='w', encoding=文件编码['attendance']) as file:
                    pass
                历史被点到, 当前被点到 = [[], []]
                logging.info(text('A.AD'))
                print(黄色(text('5.02')))

            if x == 6:
                for i, j in zip([当前被点到, 历史被点到],['6.02', '6.03']):
                    比对名单 = {k for k in 总名单 if not (k in set(i))}
                    print(青色(text(j)))
                    格式化输出(比对名单)

            if x == 7:
                with open(file=文件路径['output'], mode='a', encoding=文件编码['output']) as file:
                    print(text('7.02'), 当前时间(), file=file)
                    格式化输出(当前被点到, file=file)
                    file.write('\n\n')
                logging.info(text('a.ae'))
                print(黄色(text('7.03')), 青色(文件路径['output']))

            if x == 8:
                y = 姓名输入(绿色(text('8.02')))
                print(黄色(text('8.03').center(6)))
                概率 = round(1 / len(总名单), 5)
                for i in y:
                    次数 = 历史被点到.count(i)
                    频率 = round(次数 / len(历史被点到), 5)
                    if i in 总名单:
                        condition = 青色(概率)
                    elif 次数:
                        condition = 红色(text('8.04'))
                    else:
                        condition = 红色(text('8.05'))
                        次数 = 频率 = ''
                    print(f'{蓝色(i)} | {青色(次数)} | {青色(频率)} | {condition}')
                logging.info('8')
                space()

            if x == 9:
                格式化输出(当前被点到)
                print(黄色(text('9.02')), 青色(len(当前被点到)))
                logging.info('9')

            if x == 10:
                功能打印(FUNC_dev)
                y = 取整输入(绿色(text('10.03')))
                if y not in [1, 2]:
                    continue
                成员 = set(姓名输入(绿色(text('10.04'))))
                if not 成员:
                    continue
                dev_mode = dev_map[y]
                if y == 1:
                    成员 = {i for i in 成员 if i not in 总名单}
                    总名单.update(成员); 当前名单.update(成员); 添加成员.extend(成员)
                if y == 2:
                    成员 = {i for i in 成员 if i in 总名单}
                    总名单 = 总名单.difference(成员)
                    当前名单 = 当前名单.difference(成员)
                    删除成员.extend(成员)
                with open(file=文件路径['name'], mode='w', encoding=文件编码['name']) as file:
                    for i in 总名单:
                        file.write(f'{i}\n')
                print(黄色(temp:= text(dev_mode[0])), 青色(','.join(dev_mode[1])))
                格式化输出(当前名单)
                logging.info(f'10, mode={temp}, obj={成员}')

            if x == 11:
                print(蓝色(text('11.02')))
                try:
                    startfile(文件路径['parameter'])
                    system('pause')
                except Exception as e:
                    print(红色(temp:= (text('a.aa') + str(e))))
                    logging.warning(temp)
                logging.info('11')

            if x == 12:
                open(file=文件路径['cache'], mode='w', encoding=文件编码['cache']).close()
                open(file=文件路径['attendance'], mode='w', encoding=文件编码['attendance']).close()
                rmtree(r'user\history', ignore_errors=True)
                logging.info('12')
            space()
    space()
    sleep(0.5)
