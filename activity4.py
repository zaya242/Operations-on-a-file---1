#Write a Python program to copy odd lines from one file to another file. For copying it in a new file, create a new empty file and upload it similarly as you do for the given file.

file1=open('codingal.txt','r')
file2=open('oddfile.txt','w')

cont=file1.readlines()
type(cont)
for i in range(1,len(cont)+1):
    if i%2!=0:
        file2.write(cont[i-1])
    else:
        pass 

file1.close()
file2.close()    