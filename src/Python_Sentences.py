print()
print("########### The following is While Sentences ###########")
print()

#var = 1
#while var == 1 :  # 该条件永远为true，循环将无限执行下去
    # num = input("Enter a number  :")
    # print ("You entered: ", num)

#print ("Good bye!")

count = 0
while count < 2:
    print (count, " is  less than 5")
    count = count + 1
else:
    print (count, " is not less than 5")

print()
print("########### The following is For Sentences ###########")
print()

for letter in 'Python':     # 第一个实例
    print ('当前字母 :', letter)

fruits = ['banana', 'apple',  'mango']
for fruit in fruits:        # 第二个实例
    print ('当前字母 :', fruit)
    
fruits = ['banana', 'apple',  'mango']
for index in range(len(fruits)): # 第三个实例
    print ('当前水果 :', fruits[index])

print()
print("########### The following is 质数运算  ###########")
print()  
    
for num in range(10,20):  # 迭代 10 到 20 之间的数字
    for i in range(2,num): # 根据因子迭代
        if num%i == 0:      # 确定第一个因子
            j=num/i          # 计算第二个因子
            print ('%d 等于 %d * %d' % (num,i,j))
            break            # 跳出当前循环
    else:                  # 循环的 else 部分
        print (num, '是一个质数')
        
print()
print("########### The following is 素数运算  ###########")
print()        

i = 2
while(i < 100):
    j = 2
    while(j <= (i/j)):
        if not(i%j): break
        j = j + 1
    if (j > i/j) : print (i, " 是素数")
    i = i + 1

print ("Good bye!")

print()
print("########### The following is Continue Sentences  ###########")
print()      

for letter in 'Python':     # 第一个实例
    if letter == 'h':
        continue
    print ('当前字母 :', letter)

var = 10                    # 第二个实例
while var > 0:              
    var = var -1
    if var == 5:
        continue
    print ('当前变量值 :', var)
