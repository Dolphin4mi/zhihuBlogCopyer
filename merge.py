import os

name  = 'MP1_30.md'
f_all = open(name,'x',encoding='utf-8')
linesall = []
for i in range(1,30):
    name = 'MP' + str(i) + '.md'
    f = open(name,'r',encoding='utf-8')
    lines = f.readlines()
    f.close()
    linesall.append('\n')
    linesall.append('\n')
    linesall.extend(lines)
f_all.writelines(linesall)
f_all.close()



name  = 'MP30_60.md'
f_all = open(name,'x',encoding='utf-8')
linesall = []
for i in range(30,60):
    name = 'MP' + str(i) + '.md'
    f = open(name,'r',encoding='utf-8')
    lines = f.readlines()
    f.close()
    linesall.append('\n')
    linesall.append('\n')
    linesall.extend(lines)
f_all.writelines(linesall)
f_all.close()


name  = 'MP60_90.md'
f_all = open(name,'x',encoding='utf-8')
linesall = []
for i in range(60,90):
    name = 'MP' + str(i) + '.md'
    f = open(name,'r',encoding='utf-8')
    lines = f.readlines()
    f.close()
    linesall.append('\n')
    linesall.append('\n')
    linesall.extend(lines)
f_all.writelines(linesall)
f_all.close()


name  = 'MP90_120.md'
f_all = open(name,'x',encoding='utf-8')
linesall = []
for i in range(90,120):
    name = 'MP' + str(i) + '.md'
    f = open(name,'r',encoding='utf-8')
    lines = f.readlines()
    f.close()
    linesall.append('\n')
    linesall.append('\n')
    linesall.extend(lines)
f_all.writelines(linesall)
f_all.close()


name  = 'MP120_150.md'
f_all = open(name,'x',encoding='utf-8')
linesall = []
for i in range(120,150):
    name = 'MP' + str(i) + '.md'
    f = open(name,'r',encoding='utf-8')
    lines = f.readlines()
    f.close()
    linesall.append('\n')
    linesall.append('\n')
    linesall.extend(lines)
f_all.writelines(linesall)
f_all.close()