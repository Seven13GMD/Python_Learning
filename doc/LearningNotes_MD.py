以下划线开头的标识符是有特殊意义的。以单下划线开头（_foo）的代表不能直接访问的类属性.需通过类提供的接口进行访问，
不能用"from xxx import *"而导入；

以双下划线开头的（__foo）代表类的私有成员；
以双下划线开头和结尾的（__foo__）代表python里特殊方法专用的标识，如__init__（）代表类的构造函数。

IndentationError: unexpected indent 错误是python编译器是在告诉你
"Hi，老兄，你的文件里格式不对了，可能是tab和空格没对齐的问题"，所有python对格式要求非常严格。

如果是 IndentationError: unindent does not match any outer indentation level错误表明，
你使用的缩进方式不一致，有的是 tab 键缩进，有的是空格缩进，改为一致即可。

在 python 中，for … else 表示这样的意思，for 中的语句和普通的没有区别，else 中的语句会在循环正常执行完
（即 for 不是通过 break 跳出而中断的）的情况下执行，while … else 也是一样。

Python 支持格式化字符串的输出 。尽管这样可能会用到非常复杂的表达式，
但最基本的用法是将一个值插入到一个有字符串格式符 %s 的字符串中。
在 Python 中，字符串格式化使用与 C 中 sprintf 函数一样的语法。
如下实例：
#!/usr/bin/python
print "My name is %s and weight is %d kg!" % ('Zara', 21) 

元组中只包含一个元素时，需要在元素后面添加逗号
tup1 = (50,);
元组中的元素值是不允许删除的，但我们可以使用del语句来删除整个元组

Python 的 time 模块下有很多函数可以转换常见日期格式。如函数time.time()用于获取当前时间戳


