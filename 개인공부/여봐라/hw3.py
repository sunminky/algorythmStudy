myfile1=open("test.txt", "r", encoding='UTF8')
lines1=myfile1.read()
print(lines1)
#myfile1.end()
myfile1.close()

myfile2=open("test.txt", "a", encoding='UTF8')
myfile2.write("\n원수는 외나무다리에서 만난다.\n")
#myfile2.end()
myfile2.close()

