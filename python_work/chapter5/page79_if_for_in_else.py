#以特殊方式跟管理员打招呼：创建一个至少包含5个用户名的列表，且其中给一个用户名为‘admin’。想象你要编写代码，在每位用户登录网站后
#都打印一条问候消息。遍历用户名列表，并向每位用户打印一条问候消息。

users_name = ['oldtree','manson','admin','johnson','rachel','sancy']
for user_name in users_name:
    print("Hello,"+user_name.title() +",welcome to our zone!")

#如果用户名为‘admin’，就打印一条特殊的问候消息，如“Hello admin，would you like to see a status report?"。
# 否则，打印一条"普通问候消息，如‘Hello Eric,thank you for logging in again’
print("\n如果用户名为‘admin’，就打印一条特殊的问候消息，如Hello admin，would you like to see a status report,否则，打印一条"
      "普通问候消息，如‘Hello Eric,thank you for logging in again’")
users_name = ['oldtree','manson','admin','johnson','rachel','sancy']
for user_name in users_name:
    if user_name == 'admin':
        print("Hello admin,would you like to see a status report?")
    else:
        print("Hello,"+user_name.title() +",thank you for logging in again")

#5-9 处理没有用户的情形：在为完成练习5-8编写的程序中，添加一条if语句，检查用户名列表是否为空。
#如果为空，就打印消息“We need to find some users!".
#删除列表中的所有用户名，确定将打印正确的消息。
print("\n\n5-9 处理没有用户的情形:")
users_name = []
if users_name:
    for user_name in users_name:
        print("Hello,"+user_name.title() +",thank you for logging in again")
else:
    print("We need to find some users!")

#5-10检查用户名：按下面的说明编写一个程序，模拟网站确保每位用户的用户名都独一无二的方式。
#创建一个至少包含5个用户名的列表，并将其命名为current_users.
#再创建一个包含5个用户名的列表，将其命名为new_users,并确保其中有一两个用户名也包含在列表current_users中。
#遍历列表new_users,对于其中的每个用户名，都检查它是否已被使用，如果是这样，就打印一条消息，指出需要输入别的用户名；否则打印一条消息
#指出这个用户名未被使用。
#确保比较时不区分大小写；换句话说，如果用户名‘John’已被使用，应拒绝用户名‘JHON’.
print("\n\n5-10检查用户名,按下面的说明编写一个程序，模拟网站确保每位用户的用户名都独一无二的方式:")
current_users = ['oldtree','admin','john','rachel','sancy']
new_users = ['JOHN','linda','lily','admin','johnson']
for new_user in new_users:
    if new_user.lower() in current_users:
        print("Sorry,the name "+"'"+new_user+"'"+" have been used!Try another name")
    else:
        print("You can use this name"+"'"+new_user.lower()+"'")


#5-11序数：序数表示位置，如1st和2nd。大多数序数都以th结尾，只有1、2和3例外。
#在一个列表中储存数字1~9.
#遍历这个列表。

print("\n\n5-11序数：")
numbers = [1,2,3,4,5,6,7,8,9]
for number in numbers:
    print(number)
#在循环中使用一个if-elif-else结构，以打印每个数字对应的序数。输出内容应为1st、2nd、3rd、4th、5th、6th、7th、8th和9th，但每个序数都独占一行。

print("\n\n在循环中使用一个if-elif-else结构，以打印每个数字对应的序数。输出内容应为1st、2nd、3rd、4th、5th、6th、7th、8th和9th，但每个序数都独占一行")
numbers = [1,2,3,4,5,6,7,8,9]
for number in numbers:
    if number == 1:
        print(str(number)+"st")
    elif number == 2:
        print(str(number)+"nd")
    elif number == 3:
        print(str(number)+"rd")
    else:
        print(str(number)+"th")





