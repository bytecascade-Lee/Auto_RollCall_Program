# 自动点名程序 (Auto RollCall Program)

一个功能完善的自动点名工具，适用于课堂、会议等场景，支持随机点名、出勤记录、数据统计等功能。

## 功能特点

- 随机点名：从名单中随机选择成员，支持设置是否允许重复点名
- 名单管理：查看、添加、删除成员信息
- 出勤统计：记录每次点名结果，统计成员被点名次数和概率
- 多语言支持：支持中文和英文切换
- 语音播报：可选开启点名结果语音播报
- 结果导出：将点名结果保存到文件

## 安装说明

### 前提条件
- Python 3.6 或更高版本

### 安装依赖
```bash
pip install colorama
pip install pyttsx3
```
## 使用方法

1. 首次使用前，在`user/namelist.txt`文件中添加点名成员名单，每行一个名字
2. （可选）在`user/parameter.txt`中配置参数：
   - 是否允许重复点名（允许/不允许）
   - 是否开启语音播报（开启/关闭）
   - 语言设置（中文/English）
3. 运行主程序：
```bash
python main.py
```
4. 根据菜单提示选择相应功能：
   - 输入数字1进行随机点名
   - 输入数字0进入更多操作菜单

## 项目结构
Auto_RollCall_Program/
├── .gitignore          # 忽略不需要纳入版本控制的文件
├── core.json           # 核心配置文件，定义文件路径和编码方式
├── main.py             # 程序入口，实现主要交互逻辑
├── user/               # 用户相关数据文件
│   ├── history/        # 历史数据（选择生成，在清除缓存时会被清空）
│   ├── namelist.txt    # 点名名单（用户需填写，否则无法正常进入工作界面）
│   ├── output.txt      # 点名结果输出文件（在清除历史点名记录时会被复制到/history/，然后被清空）
│   └── parameter.txt   # 用户参数配置
├── package/            # 核心功能模块
│   ├── __init__.py     # 包初始化文件
│   ├── config_setup.py # 配置加载与初始化
│   ├── constant.py     # 常量定义
│   └── function.py     # 工具函数
└── inner/              # 内部生成的数据文件
    ├── attendance.csv  # 出勤记录（自动生成，在清除历史点名记录时会被复制到/history/，然后被清空）
    ├── cache.log       # 程序运行日志（自动生成）
    └── language.ini    # 多语言配置


## 常见问题

1. **Q: 名单文件应该是什么格式？**
   A: 每个名字单独占一行，编码格式为GBK

2. **Q: 如何切换语言？**
   A: 在`user/parameter.txt`中修改语言设置为"中文"或"English"或者使用`功能11`修改（均对下一次生效）

3. **Q: 点名记录保存在哪里？**
   A: 所有点名记录自动保存在`inner/attendance.csv`文件中，若要查看请使用`功能3`或手动打开，以后会推出更完备的功能

4. **Q: 语音播报功能无法使用怎么办？**
   A: 请检查是否已安装pyttsx3库，或尝试更换系统默认音频设备

5. **Q: 能不能在无Python环境的设备上运行？**
   A: 暂时不可以，以后会推出`.exe`可执行文件

## 联系方式

如有任何问题或建议，请在[`Issues`](https://github.com/bytecascade-Lee/Auto_RollCall_Program/issues)中提交
