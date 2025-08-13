# <center> Changelog</center>

所有版本的变更及变更后`*.py`</font>文件的部分数据都会记录在此文件中。

## [4.3.1]  2025-8-13

### <font color=yellow>Changed</font> 
- 调整清除历史记录和清除缓存的相关操作，具体表现为：执行<font color=9C88CB>`功能5`</font>时，只清空<font color=9C88CB>`inner\attendance.csv`</font>下内容；执行<font color=9C88CB>`功能11`</font>时，清空<font color=9C88CB>`user\history`</font>、<font color=9C88CB>`inner\attendance.csv`</font>和<font color=9C88CB>`inner\cache.log`</font>全部内容。
- 优化`core.json`及`package\config_setup.py`中内容

### <font color=red>Fixed</font> 
- 修复点名结果导出时姓名偶尔打印失败的问题


### Statistic
|      <font color=cyan>文件</font>      | <font color=red>总计行数</font> | <font color=pink>代码占比</font> | <font color=green>空白占比</font> | <font color=yellow>注释占比</font> |
|:------------------------------------:|:---------------------------:|:----------------------------:|:-----------------------------:|:------------------------------:|
|      <font color=cyan>总计</font>      | <font color=red>367</font>  | <font color=pink>79%</font>  | <font color=green>17%</font>  |  <font color=yellow>4%</font>  |
|     <font color=cyan>main</font>     | <font color=red>152</font>  | <font color=pink>89%</font>  | <font color=green>10%</font>  |  <font color=yellow>1%</font>  |
| <font color=cyan>config_setup</font> |  <font color=red>79</font>  | <font color=pink>80%</font>  | <font color=green>16%</font>  |  <font color=yellow>4%</font>  |
|   <font color=cyan>constant</font>   |  <font color=red>37</font>  | <font color=pink>73%</font>  |  <font color=green>5%</font>  | <font color=yellow>22%</font>  |
|   <font color=cyan>function</font>   |  <font color=red>95</font>  | <font color=pink>69%</font>  | <font color=green>28%</font>  |  <font color=yellow>2%</font>  |
|   <font color=cyan>__init__</font>   |  <font color=red>4</font>   |  <font color=pink>0%</font>  |  <font color=green>0%</font>  | <font color=yellow>100%</font> |

## [4.3]  2025-8-13

### <font color=green>Added</font> 
- 初始版本发布，包含核心功能：
  - 随机点名（支持是否允许重复）
  - 名单管理（查看、添加、删除成员）
  - 出勤记录统计（保存到<font color=9C88CB>`inner\attendance.csv`</font>）
  - 多语言支持（中文/英文切换）
  - 语音播报点名结果
  - 点名结果导出到<font color=9C88CB>`user\output.txt`</font>
