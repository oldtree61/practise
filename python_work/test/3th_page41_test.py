#page41 sorted  reverse  len
#3-8放眼世界：想出至少5个你渴望去旅游的地方。
#将这些地方储存在一个列表中，并确保其中的元素不是按字母的顺序排列的。
#按原始排列顺序打印该列表。不要考虑输出是否整洁的问题，只管打印原始PYTHON列表。
travel_place=["Thailand","The United States","Japan","Singapore","Swiss","Virginia","Bankok"]
print(travel_place)

#使用sorted()按字母顺序打印这个列表，同时不要修改它。
print(sorted(travel_place))

#再次打印该列表，核实排列顺序未变。
print(travel_place)

#这行极其重要，使用sorted按与字母顺序相反的顺序打印这个列表，同时不要修改它。而不是只是打印列表相反的顺序！！
#reverse=True,作为参数在列表参数之后，以逗号隔开
""" 这行极其重要，使用sorted按与字母顺序相反的顺序打印这个列表，同时不要修改它。而不是只是打印列表相反的顺序！！ """
"""reverse=True,作为参数在列表参数之后，以逗号隔开"""
print(sorted(travel_place, reverse=True))

#再次打印该列表，核实排列顺序未变
print(travel_place)

#使用reverse()修改列表元素的排列顺序。打印该列表，核实排列顺序确实变了。
travel_place.reverse()
print(travel_place)

#使用reverse()再次修改列表元素的排列顺序，打印该列表，核实已恢复到原来的排列顺序。
travel_place.reverse()
print(travel_place)

#使用sort()修改该列表，使其元素按字母顺序排列。打印该列表，核实排列顺序确实变了。
travel_place.sort()
print(travel_place)

#使用sort()修改该列表，使其元素按与字母顺序相反的顺序排列。打印该列表，核实排列顺序确实变了。
travel_place.sort(reverse=True)
print(travel_place)



#3-9晚餐嘉宾：在完成3-4练习3-7时编写的程序之一中，使用len()打印一条消息，指出你邀请了多少位嘉宾来与你共进晚餐。
"""len()最后要以str的形式在该条消息中输出"""


#3-10尝试使用各个函数：想想可储存到列表中的东西，如山岳，河流，国家，城市，语言或你喜欢的任何东西。编写一个程序，在其中
#创建一个包含这些元素的列表，然后对于本章介绍的每个函数，都至少使用一次来处理这个列表。

favorite=['sancy','making money','body building','games','python','english','the unite states','california','virginia','beauty','honor','thailand','swiss','sexuality']
print("\n3-10尝试使用各个函数：想想可储存到列表中的东西，如山岳，河流，国家，城市，语言或你喜欢的任何东西。编写一个程序，在其中"
          "创建一个包含这些元素的列表，然后对于本章介绍的每个函数，都至少使用一次来处理这个列表。如下：")
print("\n1.访问列表：")


print("\n2.使用列表中的各个值：")


print("\n3.修改列表元素：")


print("\n4.在列表中添加元素：")

print("（1）在末尾添加元素：")


print("\n（2）空列表内添加元素：")


print("\n5.在列表中插入元素：")


print("\n6.在列表中删除元素：\n(1)DEL删除后无法再访问")


print("\n（2）pop()删除末尾，可再访问删除元素：")



print("\n（3）pop()赋索引后删除任意元素，可再访问删除元素：")

print("\n7.（1）remove根据目标值删除元素：")

print("\n7.（2）remove储存在变量后删除元素：")


print("\n8.sort对列表永久排序以及永久反向排序")

print("\n9.sorted对列表临时排序以及临时反向排序")

print("\n9.确定列表长度：")




