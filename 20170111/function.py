'''
mylist=[7,8,9,10]
def changefuc(newlist):
    newlist.append([1,2,3,4])
    print("newlist: ",newlist)
    return


changefuc(mylist)
print("mylist: ",mylist)
'''
'''
#关键字参数
def keypra(keypra1,keypra2):
    print("Sum: ",keypra1+keypra2)
    print("sub: ",keypra1-keypra2)
    return

keypra(keypra2=20, keypra1=100)
'''

#不定长参数
def printinfo (arg1,*arg2):
    print("print the value: ",arg1)
    for i in arg2:
        print(i)
    return 

printinfo(20)
printinfo("nothing","hehe","heihei")


'''
#lamda函数

sum=lambda arg1,arg2:arg1+arg2;
print(sum(10,20))
'''
total =0
def sum(total):
    total=20+30;
    print("函数内部的total: ",total)
    return ;
sum(total)
print("函数外部的total: ",total)


