import os
import time
# 1.需要备份的文件与目录将被指定在一个列表中
# 列 Windows下：
surce = ['"F:\\new"','c:\\Code']
# 列如在MAc os x 与Linux下
# source = ['/users/swa/notes']
# 在这里要注意到我们必须在字符串中使用的双引号
# 用以括起来其中的包含空格的名称


# 备份文件必须存储在一个主备份目录中 列 Windows下
target_dir = 'F:\\new'
# 又列如在MAC OS X 和LINUX 下
# target_dir = '/User/swa/backup'
# 要记得将这里的目录地址修改至你使用的路径
# 如果目录目标不存在创建目录
if not os.path.exists(target_dir):
    os.mkdir(target_dir)  #创建目录

# 备份文件将打包成压缩 ZIP文件
# 将当前的日期作为主备份目录下的子目录名称
today = target_dir +os.sep + time.strftime('%Y%m%d')
# 将当前的时间作为 ZIP 文件的文件名
now = time.strftime('%H%M%S')

# ZIP 文件的名称格式
target = today + os.sep + now +'.zip'
# 如果子目录尚不存在则创建一个
if not os.path.exists(today):
    os.mkdir(today)
    print('succesfully created directory',today)

# 使用zip命令将文件打包成zip格式
zip_command = 'zip -r {0} {1}'.format(target,' '.join(source))

# 运行备份
print('zip command is :')
print(zip_command)
if os.system(zip_command) == 0:
    print('Successful backup to',target)
else:
    print('backup FAILED')