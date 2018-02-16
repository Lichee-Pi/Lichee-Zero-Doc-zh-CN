# coding: utf-8
import sys
import datetime

# 此二句仅在python2有效
reload(sys)  # 重新载入sys.setdefaultencoding 方法
sys.setdefaultencoding('utf-8')

# 状态定义
header_list = 0
value_matrix = 1
space_line = 2

lastline = 2


def split_file(filename):  # 分割原始文件
    f = open(filename).readlines()  # 打开该原始文件，默认该文件不可修改
    new_file = open('convert_file.py', 'a+')  # 创建并打开文件，文件可写
    new_file.truncate()

    new_file.write("# coding: utf-8\r\n\n")
    global lastline
    for each_line in f:
        if len(each_line.strip()) == 0:
            if lastline == value_matrix:
                new_file.write("]\r\n\n\n\n")
            lastline = space_line
        else:
            each_line.strip()
            if lastline == space_line:
                lastline = header_list
                new_file.write("#----------------  Conver timestamp  " +
                               datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') +
                               "  ---------------#\r\n\n")
                s = [x for x in each_line.split()]
                new_file.write("writer.header_list = " + str(s).decode('string_escape') +
                               "\r\n\r\n".decode('string_escape'))
            elif lastline == header_list:
                lastline = value_matrix
                s = [x for x in each_line.split()]
                new_file.write(
                    "writer.value_matrix = [\r\n\t" + str(s).decode('string_escape') + ",\r\n")
            elif lastline == value_matrix:
                lastline == value_matrix
                s = [x for x in each_line.split()]
                new_file.write(
                    '\t' + str(s).decode('string_escape') + ",\r\n".decode('string_escape'))
    new_file.write("]\r\n")
    new_file.close()


split_file('lalala.txt')
