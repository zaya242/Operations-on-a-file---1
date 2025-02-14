file=open('codingal.txt','r')
print(file.read())
file.close()

file=open('codingal.txt','r')
print(file.read(15))
file.close()

file=open('codingal.txt','a')
file.write("\nMy name is zainab and i am 16 years old")
file.close()