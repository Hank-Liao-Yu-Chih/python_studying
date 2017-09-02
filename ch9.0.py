f = open("data.txt",'r')

for line in f.readlines():
    line = line.strip()
    print(line)
f.close()    




fo = open("write.txt","w+")
fo.write("hello jave\n")
fo.write("hello python\n")
fo.close()

fo = open("write.txt","r")
for line in fo.readlines():
	line = line.strip()
	print(line)
fo.close()