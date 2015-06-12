#!env python
#coding=utf-8
# 
# Author:       
# 
# Created Time: Mon 08 Jun 2015 09:56:46 PM EDT
# 
# FileName:     open_in_brower.py
# 
# Description:  
# 
# ChangeLog:

import subprocess
import sys

def execute_cmd(url, exe_type):
    cmd = "firefox " + exe_type + " " + url
    p = subprocess.Popen(cmd, shell=True)
    p.wait()
    

def read_url(file_name):
    count = 0
    exe_type = '-new-tab'
    with open(file_name, 'r') as fd:
        for line in fd:
            if count % 25 == 0:
                exe_type = '-new-window'
            line = line.strip()
            line = line.split()[0]
            execute_cmd(line, exe_type)
            count = count + 1


if __name__ == '__main__':
    file_name = sys.argv[1]
    read_url(file_name)

            

