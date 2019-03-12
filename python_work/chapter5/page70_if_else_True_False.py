#5-1条件测试：编写一系列条件测试：将每个测试以及你对其结果的预测和实际结果都打印出来。你编写的代码应类似于下面这样：
#----------------------------------------------------------------------------------------------------------------
print("----------------------------------------------------------------------------------------------------------------")
car='subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')
#----------------------------------------------------------------------------------------------------------------
print("\n----------------------------------------------------------------------------------------------------------------")
food='chicken'
print("Is food == 'chicken'? I predict True.")
print(food=='chicken')

print("\nIs food == 'rice'? I predict False.")
print(food == 'rice')
#----------------------------------------------------------------------------------------------------------------
print("----------------------------------------------------------------------------------------------------------------")


#详细研究实际结果，知道你明白了它为何为True或False。

#创建至少10个测试，且其中结果分别为True和False的测试都至少有5个。
#1.
print("\n1.")
car = 'bmw'
print(car == 'bmw')
print(car == 'audi')

#2.
print("\n2.")
car = 'Audi'
print(car == 'audi')
print(car.lower() == 'audi')


#3.
print("\n3.")
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies")
    print(requested_topping == 'anchovies')

#4.
print("\n4.")
age = 18
print(age == 18)

answer = 17
if answer != 47:
    print("That is not the correct answer.Please try again!")
    print(answer == 30)

#5.
print("\n5.")
age_0 = 18
age_1 = 27
print(age_0 <= 20)
print(age_1 >= 30)





#5-2更多的条件测试：你并非只能创建10个测试。如果你想尝试做更多的比较，可再编写一些测试，并将它们加入到conditional_tests.py中。
#对于下面列出的各种测试，至少编写一个结果为True和False的测试。

#检查两个字符串相等或不等。
print("\n5-2检查两个字符串相等或不等:")
food_0='rice'
food_1='salad'
print(food_0 == food_1)
print(food_1 == 'salad')


#使用函数lower()的测试。
print("\n使用函数lower()的测试:")
car = 'BMW'
print(car == 'bmw')
print(car.lower() == 'bmw')


#检查两个数字相等、不等、大于、小于、大于等于和小于等于。
print("\n检查两个数字相等、不等、大于、小于、大于等于和小于等于:")
number1=37
number2=26
print(number1 == number2)
print(number1 != number2)
print(number1 > number2)
print(number1 < number2)
print(number1 >= number2)
print(number1 <= number2)

#使用关键字and和or的测试。
print("\n使用关键字and和or的测试:")
number1=37
number2=26
print(number1>=number2 and number2<=number1)
print(number1>number2 or number2>number1)
print(number1>number2 and number2>number1)

#测试特定的值是否包含在列表中。
print("\n#测试特定的值是否包含在列表中:")
names=["linda","manson","kiki"]
print("sancy" in names)
print("linda"in names)

#测试特定的值是否未包含在列表中。
print("\n#测试特定的值是否未包含在列表中。")
names=["linda","manson","kiki"]
name='sancy'
if name in names:
    print("Sorry, the name have been used! Make a new name!")
else:
    print("Well,"+name.title()+", U can use this name!")

names.append('sancy')
if name in names:
    print("Sorry, the name have been used! Make a new name!")
else:
    print("Well," + name.title() + ", U can use this name!")

