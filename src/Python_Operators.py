a = 21
b = 10
c = 0

print()
print("########### The following is + ###########")
print()

c = a + b
print("c的值为:",c)

print()
print("########### The following is - ###########")
print()

c = b - a
print("c的值为:",c)

print()
print("########### The following is * ###########")
print()

c = c *(a + b)
print("c的值为:",c)

print()
print("########### The following is / ###########")
print()

c = c *(a + b) / (b - a)
print("c的值为:",c)

print()
print("########### The following is % ###########")
print()

c = a % b
print("c的值为:",c)

print()
print("########### The following is compare ###########")
print()

if ( a == b ):
    print ("1 - a 等于 b")
else:
    print ("1 - a 不等于 b")

if ( a != b ):
    print ("2 - a 不等于 b")
else:
    print ("2 - a 等于 b")

if ( a < b ):
    print ("4 - a 小于 b") 
else:
    print ("4 - a 大于等于 b")

if ( a > b ):
    print ("5 - a 大于 b")
else:
    print ("5 - a 小于等于 b")
    
if ( a <= b ):
    print ("6 - a 小于等于 b")
else:
    print ("6 - a 大于  b")

if ( b >= a ):
    print ("7 - b 大于等于 b")
else:
    print ("7 - b 小于 b")

print()
print("########### The following is Bitwise Operators ###########")
print()

a = 60            # 60 = 0011 1100 
b = 13            # 13 = 0000 1101 
c = 0

c = a & b;        # 12 = 0000 1100
print ("1 - c 的值为：", c)

c = a | b;        # 61 = 0011 1101 
print ("2 - c 的值为：", c)

c = a ^ b;        # 49 = 0011 0001
print ("3 - c 的值为：", c)

c = ~a;           # -61 = 1100 0011
print ("4 - c 的值为：", c)

c = a << 2;       # 240 = 1111 0000
print ("5 - c 的值为：", c)

c = a >> 2;       # 15 = 0000 1111
print ("6 - c 的值为：", c)

print()
print("########### The following is Operator Priority ###########")
print()

a = 20
b = 10
c = 15
d = 5
e = 0

e = (a + b) * c / d       #( 30 * 15 ) / 5
print ("(a + b) * c / d 运算结果为：",  e)

e = ((a + b) * c) / d     # (30 * 15 ) / 5
print ("((a + b) * c) / d 运算结果为：",  e)

e = (a + b) * (c / d);    # (30) * (15/5)
print ("(a + b) * (c / d) 运算结果为：",  e)

e = a + (b * c) / d;      #  20 + (150/5)
print ("a + (b * c) / d 运算结果为：",  e)
