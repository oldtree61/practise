#4-1 比萨：想出至少三种你喜欢的比萨，将其名称储存在一个列表中，再使用for循环将每种比萨的名称打印出来。
pizzas=["fruit pizza","ham pizza","sweet pizza","cheese pizza"]
for pizza in pizzas:
    print(pizza)


#修改这个for循环，使其打印包含比萨名称的句子，而不仅仅是比萨的名称。对于每种比萨，都显示一行输出，如“I like pepperoni pizza".
    print("I like "+pizza.title()+".")




#在程序末尾添加一行代码，它不在for循环中，指出你有多喜欢比萨。输出应包含针对每种比萨的信息，还有一个总结性句子，如“I really love pizza!".

print("I like "+pizzas[0].title()+"、"+pizzas[1].title()+" and "+pizzas[2].title()+".")
print("I really love pizza!")





#4-2 动物：想出至少三种有共同特征的动物，将这些动物的名称储存在一个列表中，再使用for循环将每种动物的名称都打出来。
print("\n动物：")
animals=["dog","cat","bird"]
for animal in animals:
    print(animal)

#修改这个程序，使其针对每种动物都打印一个句子，如“A dog would make a great pet".
    print("A "+animal+" would make a great pet")


#在程序末尾添加一行代码，指出这些动物的共同之处，如打印诸如“Any of these animals would make a great pet!"这样的句子。

print(animals[0]+","+animals[1]+" and "+animals[2]+" are the most faithful of human beings")
print("Any of these animals would make a great pet!")