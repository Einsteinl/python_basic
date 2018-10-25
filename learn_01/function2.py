#!/usr/bin/python
# -*- coding: UTF-8 -*-

def printinfo(arg1,*vartuple):
    "This prints a variable passed arguments"
    print("output is:")
    print(arg1)
    print("可变参数类型是：",type(vartuple))
    for var in vartuple:
        print(var)
    return 5

# 调用
i=printinfo(10)
printinfo(70,60,50)
print(i)


