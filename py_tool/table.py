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
writer = pytablewriter.RstSimpleTableWriter()
# change the stream to a string buffer to get the output as a string
writer.stream = six.StringIO()

writer.header_list = ['分区序号', '分区大小', '分区作用', '地址空间及分区名']

writer.value_matrix = [
    ['mtd0', '1MB', 'spl+uboot', '0x0000000-0x0100000 : \"uboot\"'],
    ['mtd1', '64KB', 'dtb文件', '0x0100000-0x0110000: \"dtb\"'],
    ['mtd2', '4MB', 'linux内核', '0x0110000-0x0510000 : \"kernel\"'],
    ['mtd3', '剩余', '根文件系统', '0x0510000-0x2000000 : \"rootfs\"'],
]


with open(filepath, "a+") as f:
    writer.stream = f
    writer.write_table()


# 转换结束的提示
six.print_("\nconvert finished！please open "+filepath+" to get the result.\n")
