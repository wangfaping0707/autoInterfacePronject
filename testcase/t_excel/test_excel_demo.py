# 导入读取excel表中数据的模块
import xlrd

# 打开工作簿：
# xlrd.open_workbook(excel文件路径) - 打开指定路径对应的excel文件，返回excel文件对应的工作簿对象。
workbook = xlrd.open_workbook(filename="data.xlsx")

"""
选择工作表:一个工作簿中可能包含多个工作表，上面我给的案例文件 data.xlsx 文件是一个工作簿，
里面包含了两个工作表，分别是： 和 teacher。获取excel文件内容的时候需要先确定，需要获取的数据来源于哪个工作表。
获取需要操作的sheet表格（有三种方法）:
1、通过索引获取
获取第一个sheet表格
table = workbook.sheets()[0]

2、通过索引顺序获取
通过索引获取
table = workbook.sheet_by_index(0)

3、通过sheet名称获取
通过sheet名称获取
table = workbook.sheet_by_name(sheet_name='Sheet1')

4、获取工作薄中所有sheet名称
获取工作薄中所有的sheet名称
names = workbook.sheet_names()
print(names)
"""
# 一、获取工作簿所有表格
sheets=workbook.sheet_names()
print(f'获取工作簿中所有表：{sheets}')

# 二、获取工作簿第二个sheet
sheets_two=workbook.sheet_names()[1]
print(f'获取工作簿中第二个表：{sheets_two}')

# 三、获取工作簿第一个sheet，索引
sheets_by_index_one=workbook.sheet_by_index(0)

# 四、获取工作簿第一个sheet，表名称
sheets_by_name_one=workbook.sheet_by_name('个人信息表')

# 行和列的操作
# 常用1：获取sheet中有多少行和多少列
rows = sheets_by_name_one.nrows
print(f'表多少行：{rows}')
cols = sheets_by_name_one.ncols
print(f'表多少列：{cols}')

# 常用2：获取一行中有多少列数据
num = sheets_by_name_one.row_len(0)
print(f'第一行有多少列数据：{num}')

# 常用3：获取指定行或者列中所有的数据

'''
# rowx表示是获取第几行的数据
# start_col表示从索引为多少开始，end_colx表示从索引为多少结束，
# end_colx 值为None: 表示结束没有限制
# 获取指定行中的数据并以列表的形式返回
# 需要先指定sheet工作表
table = workbook.sheet_by_name(sheet_name='视频课列表')
table_list = table.row_values(rowx=0, start_colx=0, end_colx=None)
print(table_list)
'''
sheet_list1 = sheets_by_name_one.row_values(rowx=0,start_colx=0,end_colx=None)
sheet_list2 = sheets_by_name_one.row_values(rowx=1,start_colx=0,end_colx=None)
sheet_list3 = sheets_by_name_one.row_values(rowx=2,start_colx=3,end_colx=None)
print(f'sheet_list1:{sheet_list1}')
print(f'sheet_list2:{sheet_list2}')
print(f'sheet_list3:{sheet_list3}')
print('***************************************************************************************')
'''
# colx表示是获取第几列的数据
# start_rowx表示从索引为多少开始，end_rowx表示从索引为多少结束，
# end_rowx为None表示结束没有限制
# 获取指定列中的数据并以列表的形式返回
# 需要先指定sheet工作表
table = workbook.sheet_by_name(sheet_name='视频课列表')
table_list = table.col_values(colx=0, start_rowx=0, end_rowx=None)
print(table_list)
'''
sheet_col1=sheets_by_name_one.col_values(colx=0, start_rowx=0,end_rowx=None)
sheet_col2=sheets_by_name_one.col_values(colx=1, start_rowx=0,end_rowx=None)
sheet_col3=sheets_by_name_one.col_values(colx=2, start_rowx=1,end_rowx=None)
print(sheet_col1)
print(sheet_col2)
print(sheet_col3)
print('--------------------------------------------------------------------------')

# 单元格的操作:获取指定单元格的指
'''
# 获取指定单元格内的值（第二行第一列，在python中从零开始计算序号）
# 需要先指定sheet工作表
table = workbook.sheet_by_name(sheet_name='视频课列表')
value = table.cell_value(rowx=1, colx=0)
print(value)
'''
value = sheets_by_name_one.cell(rowx=6, colx=1)
print(f'指定单元格的指：{value}')

print('**************************************************************************')
# 读取每行内容
for r in range(sheets_by_name_one.nrows):
	r_values=sheets_by_name_one.row_values(r)
	print(f'第{r}行内容：{r_values}')
print('**************************************************************************')
# 读取每列内容
for c in range(sheets_by_name_one.ncols):
	c_values=sheets_by_name_one.col_values(c)
	print(f'第{c}列内容：{c_values}')





