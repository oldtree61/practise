#7-1 汽车租赁：编写一个程序，询问用户要租赁什么样的汽车，并打印一条消息，如“Let me see if I can find you a Subaru”。
print("\n汽车租赁：编写一个程序，询问用户要租赁什么样的汽车:")

cars_type = "What kind of car you want to rent? "
car = input(cars_type)
print("Let me see if I can find you a " + car)

c = input("What kind of car you want to rent? ")
print("Let me see if I can find you a " + c)

#7-2 餐馆订位：编写一个程序，询问用户有多少人用餐。如果超过8人，就打印一条消息，指出没有空桌；否则指出有空桌。

print("\n餐馆订位：编写一个程序，询问用户有多少人用餐。如果超过8人，就打印一条消息，指出没有空桌；否则指出有空桌。")

eating_numbers = input("How many people for eating? ")
eating_numbers = int(eating_numbers)
if eating_numbers >= 8:
    print("There is not enough empty table for eating.")
else:
    print("OK,there is enough empty table for your booking")


#7-3 10的整数倍：让用户输入一个数字，并指出这个数字是否是10的整数倍。
print("\n10的整数倍：让用户输入一个数字，并指出这个数字是否是10的整数倍。")
number = input("Please input a number,and I'll tell you if it's a multiple of 10 or not. ")
number = int(number)
if number % 10 == 0:
    print("Yes,It's a number of a multiple of 10")
else:
    print("Sorry,It's not a number of a mutiple of 10.")