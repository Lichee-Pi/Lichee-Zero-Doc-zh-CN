# coding: utf-8

# 为兼容rst文件中文表格问题所用的小工具
# 如需使用，请先pip install pytablewriter
# 请参考文档 http://pytablewriter.rtfd.io/

import pytablewriter
import six
import sys

# 要写入的文件名
filepath = "table.rst"

# ---python2 有效--- #
reload(sys)  # 重新载入sys.setdefaultencoding 方法
sys.setdefaultencoding('utf-8')
# End of reload #

file1 = open(filepath, 'w+')  # 打开文件
file1.truncate()  # 清空文件内容
file1.close()

# set as rst writer
writer = pytablewriter.RstGridTableWriter()
# change the stream to a string buffer to get the output as a string
writer.stream = six.StringIO()

writer.header_list = ['SPI屏', 'zero']

writer.value_matrix = [
    ['3v3', '3v3'],
    ['GND', 'GND'],
    ['DC', 'PWM1'],
    ['RST', '3v3'],
    ['CS', 'CS'],
    ['CLK', 'CLK'],
    ['MISO', 'MISO'],
    ['MOSI', 'MOSI'],
]


with open(filepath, "a+") as f:
    writer.stream = f
    writer.write_table()


# 转换结束的提示
six.print_("\nconvert finished！please open "+filepath+" to get the result.\n")
