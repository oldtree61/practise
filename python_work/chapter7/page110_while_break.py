#7-4比萨配料:编写一个循环。提示用户输入一系列的比萨配料，并在用户输入‘quit’时结束循环。每当用户输入一种配料后，都打印一条消息，
#说我们会在比萨中添加这种配料。
print("7-4比萨配料：")
prompt = "\nPlease enter the topping of pizza: "
prompt += "\nEnter 'quit' when you are finished."

while True:
    topping = input(prompt)

    if topping != 'quit':
        print("We will add " + topping.title() + " to the topping of pizza!")
    else:
        break



#7-5电影票： 有家电影院根据观众的年龄收取不同的票价：不到3岁的观众免费；3~12岁的观众为10美元；超过12岁的观众为15美元。请
#编写一个循环，在其中询问用户的年龄，并指出其票价。
print("\n7-5电影票：")

age_prompt = "\nPlease enter your age: "

while True:
    age = int(input(age_prompt))
    if age < 3:
        price = 0
    elif age < 12:
        price = 10
    else:
        price = 15
    print("Your are "+ str(age) + " years old,your ticket rates is " + str (price) + " dollars.")
    break


#7-6三个出口：以另一种方式完成练习7-4或练习7-5，在程序中采取如下所有做法。
#在while循环中使用条件测试来结束循环。
#使用变量active来控制循环结束的时机。
#使用break语句在用户输入‘quit’时退出循环。
print("\n7-6三个出口：以另一种方式完成练习7-4或练习7-5，在程序中采取如下所有做法。")
print("#在while循环中使用条件测试来结束循环。7-4比萨配料：")

prompt = "\nPlease enter the topping of pizza: "
prompt += "\nEnter 'quit' when you are finished."

topping = ""

while topping != 'quit':        #当配料不为‘quit’的时候，不停循环，以让用户添加pizza的相关配料
    topping = input(prompt)

    if topping != 'quit':       #如果配料不为‘quit’的时候，才打印以下的句子。
       print("We will add " + topping + " to your topping of pizza!")



print("\n\n#使用变量active来控制循环结束的时机。")
prompt = "\nPlease enter the topping of pizza: "
prompt += "\nEnter 'quit' when you are finished."
active = True

while active:
    topping = input(prompt)

    if topping == 'quit':
        active = False
    else:
        print("We will add " + topping + " to your topping of pizza!")



print("\n\n#使用break语句在用户输入‘quit’时退出循环。")

prompt = "\nPlease enter the topping of pizza: "
prompt += "\nEnter 'quit' when you are finished."

while True:
    topping = input(prompt)
    if topping == 'quit':
        break
    else:
        print("We will add " + topping + " to your topping of pizza!")



#7-7无限循环：编写一个没完没了的循环，并运行它（要结束该循环

print("\n7-7无限循环：")

x = 0
while x < 10:
    x += 1
    print(x)






