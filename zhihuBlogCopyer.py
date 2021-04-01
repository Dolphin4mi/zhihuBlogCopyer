# Author: dolphin
# copy all the zhihu's blog into a markdown text,and translate the equations to the 'tex'
# Usage:
# 	1. copy all the content of the blog to a text file '.txt' or '.md'
# 	2. run this code with the filename = 'filename.txt' or 'filename.md'
# 	3. modify some backslash error

import sys
from urllib.parse import unquote

# filename = '1.md'
filename = sys.argv[1]
print('正在处理....')

f = open(filename, 'r+', encoding="utf-8")

lines = f.readlines()
f.close()

# 构造字典，用来解码url
key = []
for i in range(16 * 16):
	key.append("%" + str(hex(i))[2:4].rjust(2, '0').upper())
	print(key[i])

# 处理每一行
for lineloc in range(len(lines)):

	line = str(lines[lineloc])

	while "![[公式]]" in line:
		startkuohaoLoc = line.find("![[公式]]")
		line = line.replace("![[公式]](https://www.zhihu.com/equation?tex=", "$",1)

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
		line = line.replace('+',' ')

		for i in range(len(key)):
			while (key[i] in line[startkuohaoLoc:endkouhaoLoc]):
				shorttxt = line[startkuohaoLoc:endkouhaoLoc]
				shorttex = unquote(shorttxt) # 解码
				len_decreased = len(shorttxt)- len(shorttex)
				# line = line[:startkuohaoLoc] + line[startkuohaoLoc:endkouhaoLoc].replace(key[i], value[i], 1) + line[endkouhaoLoc:]
				line = line[:startkuohaoLoc] + shorttex + line[endkouhaoLoc:]
				endkouhaoLoc -= len_decreased

	while('$ ' in line):
		startLoc = line.find('$ ')
		line = line[:startLoc] + '$' + line[startLoc+2:]
	lines[lineloc] = line

# 调整整体结构
for lineloc in range(len(lines)):
	if lineloc!=0:
		oldline = line
	line = str(lines[lineloc])
	if lineloc!=0 and oldline[len(oldline)-1]=='\n' and line[0]=='$' and line[len(line)-2]=='$':
		line = line.replace('$',"\n$$\n")
	lines[lineloc] = line

# 写文件
f = open(filename, 'w', encoding="utf-8")
f.writelines(lines)
f.close()
print('处理完成，没有出错哦0.0')
