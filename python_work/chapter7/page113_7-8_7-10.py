#7-8熟食店：创建一个名为sandwich_orders的列表，在其中包含各种三明治的名字；再创建一个名为finished_sandwiches的空列表。
#遍历列表sandwich_orders,对于其中的每种三明治，都打印一条消息，如I made your tuna sandwich,并将其移到列表finished_sandwiches.
#所有三明治都制作好后，打印一条消息，将这些三明治列出来。

sandwich_orders = ['tuna sandwich','egg sandwich','tomato sandwich','ham sandwich']
finished_sandwiches = []
while sandwich_orders:
    sandwich_order = sandwich_orders.pop()
    finished_sandwiches.append(sandwich_order)
    print("I made your " + sandwich_order + ".")

print("\nAll the  sandwiches have been made were: ")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich)


#7-9五香烟熏牛肉（pastrami)卖完了：使用为完成练习7-8而创建的列表sandwich_orders,并确保‘pastrami’在其中至少出现了三次。
#在程序开头附近添加这样的代码：打印一条消息，指出熟食店的五香烟熏牛肉卖完了；再使用一个While循环将列表sandwich_orders中的
# ‘pastrami’都删除。确认最终的列表finished_sandwiches中不包含‘pastrami'.
print("\n7-9五香烟熏牛肉（pastrami)卖完了：")
sandwich_orders = ['pastrami','tuna sandwich','egg sandwich','pastrami','tomato sandwich','ham sandwich','pastrami',]
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print(sandwich_orders)


#7-10梦想的度假胜地：编写一个程序，调查用户梦想的度假胜地。使用类似于“If you could visit one place in the world,where
#would you go?"的提示，并编写一个打印调查结果的代码块。
print("\n#7-10梦想的度假胜地：")

vacationland = {}

active = True
while active:
    name = input("\nWhat is your name? ")
    place = input("\nWhere are you going during the vacation? ")
    vacationland[name] = place
    repeat = input("\nEnter the 'quit' to quit this page")
    if repeat == 'quit':
        active = False
print("\nThe vacationland are : ")
for name ,place in vacationland.items():
    print(name.title() + " going to " + place.title() + " during vacation.")

#dc
