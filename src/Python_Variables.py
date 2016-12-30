counter = 100 # 赋值整型变量
miles = 1000.0 # 浮点型
name = "John" # 字符串

cut_str = name[0:2]

print (counter)
print (miles)
print (name)
print (cut_str)

print()
print("########### the following is String ###########")
print()
str_t = "Hello World!"

print(str_t[2:])
print(str_t+str_t)
print(str_t*3)
print(str_t[0])

#List 列表
print()
print("########### the following is List ###########")
print()
lis = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']
ttlist = ['jqi',lis,tinylist,'qi']

print (lis) # 输出完整列表
print (lis[0]) # 输出列表的第一个元素
print (lis[0:3]) # 输出第二个至第三个的元素 
print (lis[2:]) # 输出从第三个开始至列表末尾的所有元素
print (tinylist * 2) # 输出列表两次
print (lis + tinylist) # 打印组合的列表
print (ttlist)
print (ttlist[1:2])

#tuple_t 元组
print()
print("########### the following is tuple_t ###########")
print()
tuple_t = ( 'abcd', 786 , 2.23, 'john', 70.2 )
tinytuple_t = (123, 'john')

print (tuple_t) # 输出完整元组
print (tuple_t[0]) # 输出元组的第一个元素
print (tuple_t[1:3]) # 输出第二个至第三个的元素 
print (tuple_t[2:]) # 输出从第三个开始至列表末尾的所有元素
print (tinytuple_t * 2) # 输出元组两次
print (tuple_t + tinytuple_t) # 打印组合的元组

#dict_tionary 字典
print()
print("########### the following is dict_tionary ###########")
print()
dict_t = {}
dict_t['one'] = "This is one"
dict_t[2] = "This is two"

tinydict_t = {'name': 'john','code':6734, 'dept': 'sales'}


print (dict_t['one']) # 输出键为'one' 的值
print (dict_t[2]) # 输出键为 2 的值
print (tinydict_t) # 输出完整的字典
print (tinydict_t.keys()) # 输出所有键
print (tinydict_t.values()) # 输出所有值
