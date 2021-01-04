# Author: dolphin
# copy all the zhihu's blog into a markdown text,and translate the equations to the 'tex'
# Usage:
# 	1. copy all the content of the blog to a text file '.txt' or '.md'
# 	2. run this code with the filename = 'filename.txt' or 'filename.md'
# 	3. modify some backslash error
filename = '2.md'
f = open(filename, 'r+', encoding="utf-8")

lines = f.readlines()
f.close()

for lineloc in range(len(lines)):
	print("hang:", lineloc)
	print(lines[lineloc])

	line = str(lines[lineloc])

	while "![[公式]]" in line:
		stratkuohaoLoc = line.find("![[公式]]")
		line = line.replace("![[公式]](https://www.zhihu.com/equation?tex=", "$",1)

		countkuohao = 1
		endkouhaoLoc = stratkuohaoLoc
		while (countkuohao != 0):
			# print("buwei0")
			if line[endkouhaoLoc] == ")":  # 如果是右括号，则记数减1
				countkuohao -= 1
			if line[endkouhaoLoc] == "(":
				countkuohao += 1  # 如果是左括号，记数加1
			endkouhaoLoc += 1
		line = list(line)
		line[endkouhaoLoc - 1] = "$"

		line = "".join(line)
		line = line.replace('+',' ')
		key = ['%20','%22','%23','%25','%26','%28','%29','%2A','%2B','%2C','%2F','%3A','%3B','%3C','%3D','%3E','%3F','%40','%5B','%5C','%5D','%7C','%5E','%7B','%7C','%7D']
		value = [' ','"','#','%','&','(',')','*','+',',','/',':',';','<','=','>','?','@','[','\\',']','|','^','{','|','}']
		for i in range(len(key)):
			while (key[i] in line[stratkuohaoLoc:endkouhaoLoc]):
				line = line[:stratkuohaoLoc] + line[stratkuohaoLoc:endkouhaoLoc].replace(key[i], value[i], 1) + line[endkouhaoLoc:]
				endkouhaoLoc -= 2
				if i==17:
					endkouhaoLoc += 1
	while('$ ' in line):
		startLoc = line.find('$ ')
		line = line[:startLoc] + '$' + line[startLoc+2:]
	lines[lineloc] = line

for lineloc in range(len(lines)):
	print("hang:", lineloc)
	if lineloc==142:
		print(1)
	print(lines[lineloc])
	if lineloc!=0:
		oldline = line
	line = str(lines[lineloc])
	if lineloc!=0 and oldline=='\n' and line[0]=='$' and line[len(line)-2]=='$':
		line = line.replace('$',"\n$$\n")
	lines[lineloc] = line

print(lines)
f = open(filename, 'w', encoding="utf-8")
f.writelines(lines)
f.close()

