'''
大学同学聚会，同桌吃饭，我们都是人，都有吃饭、喝饮料这些行为，但是毕业之后大家都做了不同的工作，有的当了会计、有的做了程序员
现在需要用python来描述：
a是程序员，a正在吃饭
b是会计，b正在喝饮料
提示（classmate为父类，工作为子类，行为用方法定义）
'''


class classmate:
    
    behavior="drink"
    
    def __init__(self):
        print("************")
    def setbehavior(self,ss):
        classmate.behavior=ss
    
    def printinfo(self):
        print("The JobName: ",classmate.__name__)
        print("Bheavior: ",classmate.behavior)

class programmer(classmate):
    def __init__(self):
        print("*************")
    def printinfo(self):
        print("The JobName: ",programmer.__name__)
        print("Bheavior: ",programmer.behavior)

class audit(classmate):
    def __init__(self):
        print("*************")
    def printinfo(self):
        print("The JobName: ",audit.__name__)
        print("Bheavior: ",audit.behavior)

a1=programmer()
a1.setbehavior("drink")
a1.printinfo()

a2=audit()
a2.setbehavior("eat")
a2.printinfo()
        
         
    