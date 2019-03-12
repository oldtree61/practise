#4-3 数到20：使用一个for循环打印数字1-20（含）。
for numbers in range(1,21):
    print(numbers)

#4-4一百万：创建一个列表，其中包含数字1~1000000，再使用一个for循环将这些数字打印出来（如果输出的时间太长，按Ctrl+C停止输出，
# 或关闭输出窗口）
biglist=[]
for number in range(1,101):
    biglist.append(number)
    print(number)

#或者用列表解析法：
print("\n或者用列表解析法：")
biglist=[number for number in range(1,101)]
print(biglist)



#4-5计算1~1000000的总和：创建一个列表，其中包含数字1~1000000，再使用min()和max()核实该列表确实是从1开始，到1000000结束的。
# 另外对这个列表调用函数sum(),看看PYTHON将一百万个数字相加需要多长时间。
lists2=[number for number in range(1,1000001)]
print(min(lists2))
print(max(lists2))
print(sum(lists2))

#4-6奇数：通过给函数range()指定第三个参数来创建一个列表，其中包含1--20的奇数；再使用一个for循环将这些数字都打印出来。
"""重点：！！！不要用函数list命名列表名字，否则无法调用list函数！！！！！因之前的代码用了list作为列表名，所以无法调用，之后更改
后该题目中的list方可调用"""
print("\n重点：！！！不要用函数list命名列表名字，否则无法调用list函数！！！！！因之前的代码用了list作为列表名，所以无法调用，之后更改"
       "后该题目中的list方可调用")
numbers=list(range(1,21,2))  #从1开始数，然后不断加2,1+2=3,3+2=5,5+2=7,7+2=9……
print(numbers)


#4-7 3的倍数：创建一个列表，其中包含3--30内能被3整除的数字；再使用一个for循环将这个列表中的数字都打印出来。
print("\n重点！！！3的倍数：")
list3=[number3 for number3 in range(3,31,3)]
print(list3)

#4-8 立方：将同一个数字乘三次称为立方。例如，在PYTHON中，2的立方用2**3表示。请创建一个列表，其中包含前10个整数（即1--10）的立方
#再使用一个for循环将这些立方数都打印出来。
list4=[]
for number4 in range(1,11):
    cube=number4**3    #cube是立方的意思
    list4.append(cube)
print(list4)           #如果此行缩进的话就是从1的立方开始不停循环打印，但如果不缩进的话就只打印一行

#4-9 立方解析：使用列表解析生成一个列表，其中包含前10个整数的立方。

list5=[number5**3 for number5 in range(1,11)]
print(list5)
