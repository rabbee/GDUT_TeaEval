#!/usr/bin/python3
# 
# 使用说明
# 编辑同目录下的login.py文件
# 在account处填入校园网账号
# 在password处填入密码
# 命令行下输入python main.py
#

from login import *
from teacher_evaluation import *

def main():
    s = login()
    submit(s)
    pass

if __name__ == '__main__':
    main()  