import os
import time


# name = sys.argv[1]

def read_md_file(md_name):
    print('正在读入', md_name, '....')
    f = open(md_name, 'r+', encoding="utf-8")
    lines = f.readlines()
    f.close()
    print('读入完毕', md_name, '....')
    return lines


def inline_math_to_bule(md_name, lines):
    for lineloc in range(len(lines)):
        line = str(lines[lineloc])

        end_now = 0
        while r"$" in line[end_now:] and r"$$" != line[0:2]:
            startkuohaoLoc = end_now + line[end_now:].find(r"$")
            endkuohaoLoc = startkuohaoLoc + line[startkuohaoLoc + 1:].find(r"$")

            math_old = line[startkuohaoLoc: endkuohaoLoc + 2]
            math_new = r"$\textcolor{bule}{" + line[startkuohaoLoc + 1: endkuohaoLoc + 1] + r"}$"

            line = line.replace(math_old, math_new, 1)
            end_now = endkuohaoLoc - len(math_old) + len(math_new) + 2
        lines[lineloc] = line
    return lines


def outline_math_to_bule(md_name, lines):
    lineloc = 0
    waiting_for_end = False
    paired = False
    endDollar = 0
    lines_len = len(lines)
    while lines_len>lineloc:
        line = str(lines[lineloc])
        if line[0:2] == r"$$" and not waiting_for_end:
            startDollar = lineloc
            waiting_for_end = True
            lineloc = lineloc + 1
            continue
        if line[0:2] == r"$$" and waiting_for_end:
            endDollar = lineloc
            waiting_for_end = False
            paired = True
        if paired:
            lines.insert(startDollar+1, "\\textcolor{bule}{\n")
            lines.insert(endDollar+1, "}\n")
            lineloc = lineloc+3
            paired = False
        if not paired:
            lineloc = lineloc + 1
        lines_len = len(lines)
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


if __name__ == "__main__":
    global error_global
    error_global = 0
    # md_name = sys.argv[1]
    md_name = "all.md"
    lines = read_md_file(md_name)
    lines = inline_math_to_bule(md_name, lines)
    lines = outline_math_to_bule(md_name, lines)
    write_md_file(md_name, lines)
