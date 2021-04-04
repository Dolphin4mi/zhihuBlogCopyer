# Author: dolphin
# copy all the zhihu's blog into a markdown text,and translate the equations to the 'tex'
# Usage:
# 	1. copy all the content of the blog to a text file '.txt' or '.md'
# 	2. run this code with the filename = 'filename.txt' or 'filename.md'
# 	3. modify some backslash error
import os
import re
import sys
import time
import urllib
import urllib.request
from urllib.parse import unquote

def read_md_file(md_name):
    print('正在读入', sys.argv[1], '....')
    f = open(md_name, 'r+', encoding="utf-8")
    lines = f.readlines()
    f.close()
    print('读入完毕', md_name, '....')
    return lines


# 重写公式
def construct_equation(lines):
    # error_global全局错误描述
    global error_global

    # 构造字典，用来解码url
    key = []
    for i in range(16 * 16):
        key.append("%" + str(hex(i))[2:4].rjust(2, '0').upper())

    # 处理每一行
    for lineloc in range(len(lines)):
        line = str(lines[lineloc])
        while "![[公式]]" in line:
            startkuohaoLoc = line.find("![[公式]]")
            line = line.replace("![[公式]](https://www.zhihu.com/equation?tex=", "$", 1)

            # 匹配括号
            countkuohao = 1
            endkouhaoLoc = startkuohaoLoc
            while (countkuohao != 0):
                if line[endkouhaoLoc] == ")":  # 如果是右括号，则记数减1
                    countkuohao -= 1
                if line[endkouhaoLoc] == "(":
                    countkuohao += 1  # 如果是左括号，记数加1
                endkouhaoLoc += 1
            line = list(line)
            line[endkouhaoLoc - 1] = "$"

            line = "".join(line)
            line = line.replace('+', ' ')

            for i in range(len(key)):
                while (key[i] in line[startkuohaoLoc:endkouhaoLoc]):
                    shorttxt = line[startkuohaoLoc:endkouhaoLoc]
                    shorttex = unquote(shorttxt)  # 解码
                    len_decreased = len(shorttxt) - len(shorttex)
                    # line = line[:startkuohaoLoc] + line[startkuohaoLoc:endkouhaoLoc].replace(key[i], value[i], 1) + line[endkouhaoLoc:]
                    line = line[:startkuohaoLoc] + shorttex + line[endkouhaoLoc:]
                    endkouhaoLoc -= len_decreased

        while ('$ ' in line):
            startLoc = line.find('$ ')
            line = line[:startLoc] + '$' + line[startLoc + 2:]
        lines[lineloc] = line

    # 调整整体结构
    for lineloc in range(len(lines)):
        if lineloc != 0:
            oldline = line
        line = str(lines[lineloc])
        if lineloc != 0 and oldline[len(oldline) - 1] == '\n' and line[0] == '$' and line[len(line) - 2] == '$':
            line = line.replace('$', "\n$$\n")
        lines[lineloc] = line
    return lines


def requestImg(url, workpath):
    global error_global
    img_src = url
    try:
        filepath, _ = urllib.request.urlretrieve(url=img_src, filename=workpath)
    except:
        print('保存图片失败url=', url)
        error_global = 1


# 下载图片的函数
def download_img(lines):

    # 匹配图片url
    print('正在下载图片....')
    reg = r'\(https://pic.*?\.(jpg|png|gif|jpeg|bmp)+.*?\)'  # 其中的问号是最短匹配，适用于每行存在多个url图片
    #reg = re.compile(r'\(https://.*?\.(jpg|png|gif|jpeg|bmp)+.*?\)')  # 其中的问号是最短匹配，适用于每行存在多个url图片
    # 保存文件夹
    savepath = sys.argv[1][:-3] + '.assets'
    if not os.path.exists(savepath):
        os.makedirs(savepath)
    # 下载图片
    imgcount = 0
    for lineloc in range(len(lines)):
        line = lines[lineloc]
        while re.search(reg, line):
            match_loc = re.search(reg, line).span()
            url = line[match_loc[0] + 1: match_loc[1] - 1]
            from urllib.parse import urlsplit
            imgname = os.path.join(savepath, os.path.basename(urlsplit(url).path))
            requestImg(url, imgname)
            imgcount += 1
            print('下载第', imgcount, '张图片', imgname)
            line = line[:match_loc[0] + 1] + imgname + ')' + line[match_loc[1]:]
        lines[lineloc] = line
    return lines


# 写文件
def write_md_file(filename, lines):
    global error_global
    f = open(filename, 'w', encoding="utf-8")
    f.writelines(lines)
    f.close()
    if 0 == error_global:
        print('\033[32m处理完成，没有出错哦0\033[0m')
    else:
        print('\033[32m处理有问题，sorry\033[0m')
        time.sleep(3)


if __name__=="__main__":
    global error_global
    error_global = 0
    md_name = sys.argv[1]
    lines = read_md_file(md_name)
    lines = construct_equation(lines)
    lines = download_img(lines)
    write_md_file(md_name, lines)
