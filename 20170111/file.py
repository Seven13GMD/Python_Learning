fo=open("filetest.txt","w+")
print("filename: ",fo.name)
print("ifclosed：",fo.closed)
print("filemode: ",fo.mode)
fo.write("This is the first python program about file O/I.\nThis is the second lines!\n")
position=fo.tell()
print("当前位置： ",position)
position=fo.seek(0,0)
print("当前位置： ",position)
content=fo.readlines()
for i in content:
    print(i)
fo.close()
print("ifclosed：",fo.closed)