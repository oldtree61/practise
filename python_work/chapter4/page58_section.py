#4-10切片：选择你在本章编写的一个程序，在末尾添加几行代码，以完成如下任务。

items_list=["car","house","money","cash","computer","motorcycle","iphone","ipad","iwatch"]
print("The first three items in the list are:")
print(items_list[:3])#打印消息"The first three items in the list are:",再使用切片来打印列表的前三个元素

print("Three items from the middle of the list are:")#打印消息"Three items from the middle of the list are:"再使用切片来打印列表中间的三个元素。
print(items_list[3:6])

print("The last three item in the list are:")#打印消息"The last three item in the list are:"，再使用切片来打印列表中末尾的三个元素。
print(items_list[-3:])

#4-11你的比萨和我的比萨：在你为完成练习4-1而编写的程序中，创建比萨列表的副本。并将其存储到变量friend_pizzas中，再完成如下任务。
my_pizzas=["fruit pizza","ham pizza","sweet pizza","cheese pizza"]
friend_pizzas=my_pizzas[:]  #创建比萨列表的副本。并将其存储到变量friend_pizzas中

my_pizzas.append("kiki pizza")#在原来的比萨列表中添加一种比萨。

friend_pizzas.append("other pizza")#在列表friend_pizzas中添加另一种比萨。

#核实你有两个不同的列表。为此，打印消息"My favorite pizzas are:",再使用一个for循环来打印第一个列表；打印消息"My friend's favorite
#pizzas are:",再使用一个for循环来打印第二个列表。核实新增的比萨被添加到了正确的列表中。
print("My favorite pizzas are:")
for pizza in my_pizzas:   #使用一个for循环来打印第一个列表；
    print(pizza)
print(my_pizzas)

print("\nMy friend's favorite pizzas are:")
for f_pizza in friend_pizzas: #再使用一个for循环来打印第二个列表。
    print(f_pizza)
print(friend_pizzas)

#4-12使用多个循环：在本节中，为节省篇幅，程序foods.py的每个版本都没有使用for循环来打印列表，请选择一个版本的food.py,再其中编写
#两个for循环，将各个食品列表都打印出来。

my_foods=["pizza","falafel","carrot cake"]
for food in my_foods:
    print(food)
print(my_foods)

friend_foods=my_foods[:]
my_foods.append("banana")
friend_foods.append("cow")


for food in my_foods:
    print(food)
print(my_foods)

for f_food in friend_foods:
    print(f_food)
print(friend_foods)

for food in my_foods[:2]:
    print(food.title())

for f_food in friend_foods[2:]:
    print(f_food.upper())