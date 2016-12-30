##以下是python的函数部分

#函数定义
print("----------函数定义----------")
def SystemOut(content):
    "输出传入的字符串"
    print(content)
    return 

SystemOut("Hello World")
SystemOut("BIU~BIU~BIU~")

#函数调用
print("----------函数调用----------")
def changeList( mylist ):
    "修改传入的列表"
    mylist.append([1,2,3,4]);
    print ("inside value: ", mylist)
    return
 
# 调用changeList函数
mylist = [10,20,30]
changeList( mylist )
print ("outside value: ", mylist)

#关键字参数
print("----------以下是关键字参数----------")
def printinfo( name, age ):
    "打印任何传入的字符串"
    print ("Name: ", name)
    print ("Age : ", age)
    return
 
#调用printinfo函数
printinfo( age=30, name="Jackson" );

#缺省参数
print("----------以下是缺省参数----------")
def printDefaultInfo( name, age = 35 ):
    "打印任何传入的字符串"
    print ("Name: ", name)
    print ("Age ", age)
    return
 
#调用printDefaultInfo函数
printDefaultInfo( age=30, name="Jackson" )
printDefaultInfo( name="Jackson" )

#不定长参数
print("----------以下是不定长参数----------")
def printVarInfo( arg1, *vartuple ):
    "打印任何传入的参数"
    print ("输出: ")
    print (arg1)
    for var in vartuple:
        print (var)
    return
 
# 调用printVarInfo 函数
printVarInfo( 10 )
printVarInfo( 70,60,80,100)

#匿名函数
print("----------匿名函数----------")
summ = lambda arg1, arg2: arg1 + arg2
 
# 调用sum函数
print ("相加后的值为 : ", summ( 10, 20 ))
print ("相加后的值为 : ", summ( 20, 20 ))

#return语句
print("----------return语句----------")
def calSum( arg1, arg2 ):
    # 返回2个参数的和."
    total = arg1 + arg2
    print ("arg1 : ", arg1 )
    print ("arg2 : ", arg2 )
    return total
 
# 调用calSum函数
print ("total : ", calSum( 10, 20 )) 

#全局变量和局部变量
print("----------全局变量和局部变量----------")
total = 0  # 这是一个全局变量
def sum_variable( arg1, arg2 ):
    #返回2个参数的和"
    total = arg1 + arg2;    #total在这里是局部变量
    print ("函数内是局部变量 : ", total)
    return total
 
#调用sum_variable函数
sum_variable( 10, 20 )
print ("函数外是全局变量 : ", total)