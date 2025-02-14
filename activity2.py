file=open('codingal.txt','r')
#read only first line of the file

print(file.readline())
file.close()



file=open('codingal.txt','r')
#read first 5 lines of the file

print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
file.close()

file=open('codingal.txt','r')
#loop through the file

for line in file:
    print(line)
file.close()    