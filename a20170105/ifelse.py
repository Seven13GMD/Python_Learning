#if else 条件语句
'''
flag=False
name='Python1'
if name =='Python':
    flag=True
    print ("Hello ,boss!")
else:
    print ("huaiyin")
'''
from _ast import Num
from getpass import _raw_input

'''
num=5
if num == 5:
    print("My")
elif num==3:
    print("Name")
elif num==1:
    print("What")
else:
    print("Sad")
'''

'''
num1=10

if (num1>0 and num1<5) or (num1>8 and num1<15):
    print("Test1")
else:
    print("Error")
'''
'''
num2="hehe"
if num2=="hehe":print("你在说啥")
print("hengheng")  
'''

#python 循环语句
'''
num3=[1,3,5,6,2,8,12,3,4,9]
even=[]
odd=[]
while len(num3)>0:
    num4=num3.pop();
    if num4%2==0:
        even.append(num4)
    else:
        odd.append(num4)
print(num3)
print(even)
print(odd)
'''
'''
num5=0
while(num5<10):
    print("The num5 is ",num5)
    num5=num5+1
print("end")
'''

'''
num6=1
while (num6<10):
    num6=num6+1
    if num6%2==0:
        continue
    print(num6)

print("break")
num7=8
while(num7>1):
    num7=num7-1
    print(num7)
    if num7==4:
        break
'''
'''
flag=True
while f2lag==True:
    num8=_raw_input("Enter a number :")
    print("You enter :" ,num8)

print("ByeBye")
'''
#for循环
'''
for letter in "Python":
    print("当前字母： ",letter)

city=["Beijing","Shanghai","Tianjin","Hebei"]
for city1 in city:
    print(city1)

for index in range(len(city)):
    print("城市： ", city[index])
'''
#寻找质数

'''
for num9 in range(10,20):
    for i in range(2,num9):
        if num9%i==0:
            j=num9/i
            print("%d equals %d * %d" % (num9,i,j))
            break;
    else:
        print(num9 , "是个质数")
'''

#字符串
print("http:\\\\")
print("\a")

errHTML = '''
<HTML><HEAD><TITLE>
Friends CGI Demo</TITLE></HEAD>
<BODY><H3>ERROR</H3>
<B>%s</B><P>
<FORM><INPUT TYPE=button VALUE=Back
ONCLICK="window.history.back()"></FORM>
</BODY></HTML>'''

print(errHTML)




        
    

        
    