#coding=utf-8
import numpy

class Employee:
    """所有员工的基类
    哈哈
    """
    empCount=0

    def __init__(self,name,salary,age):
        self.name=name
        self.salary=salary
        self.age=age

    def displayCount(self):
        print("Total Employee %d"% Employee.empCount)

    def displayEmployee(self):
        print("Name:",self.name,",Sakary:",self.salary)


# emp01 = Employee("zhangsan",10000,18)
# print(emp01.name)
# print(emp01.salary)
# emp01.displayCount()
# emp01.displayEmployee()

emp01=Employee("zhangsan",10000,18)
del emp01.age #删参数
# print(emp01.age) #报错，emp01这个对象没有这个参数
attr =getattr(emp01,"age",None)  #getattr() 函数用于返回一个对象属性值 age 不存在但设置了默认值
print(attr)