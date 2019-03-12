#5-3外星人颜色#1：假设在游戏中刚射杀了一个外星人，请创建一个名为alien_color的变量，并将其设置为‘green'、‘yello’或‘red’。
alien_color = 'green'


if alien_color == 'green':   #编写一条if语句，检查外星人是否是绿色的；如果是，就打印一条消息，指出玩家获得了5个点。
    print("U got 5 points!")

 #编写这个程序的两个版本，在一个版本中上述测试通过了，而在另一个版本中未通过（未通过测试时没有输出）。
alien_color = 'yellow'
if alien_color == 'red':
    print("U got 5 point")


#5-4外星人颜色#2：像练习5-3那样设置外星人的颜色，并编写一个if-else结构。
alien_color = 'red'
if alien_color == 'green':  #注意是双等号，双等号是询问是否！
    print("U just shoot a alien in green, U got 5 points!")
else:
    print("U don't shoot the alien in green,U got no points!")
#如果外星人是绿色的，就打印一条消息，指出玩家因射杀该外星人获得了5个点。
alien_color = 'green'
if alien_color == 'green':
    print("U just shoot a alien in green, U got 5 points!")
else:
    print("U don't shoot the alien in green,U got no points!")
#如果外星人不是绿色的，就打印一条消息，指出玩家获得了10个点。
alien_color = 'yellow'
if alien_color != 'green':
    print("The alien which U shoot is not in green,So you got 10 points")
#编写这个程序的两个版本，在一个版本中执行if代码块，而在另一个版本中执行else代码块。
alien_color = 'green'
if alien_color == 'green':
    print("U just shoot a alien in green, U got 5 points!")
else:
    print("The alien U shoot is not in green,So u got 10 points")


alien_color = 'red'
if alien_color == 'green':
    print("U just shoot a alien in green, U got 5 points!")
else:
    print("The alien U shoot is not in green,So u got 10 points")
#5-5外星人颜色#3：将练习5-4中的if-else结构改为if-elif-else结构。
#如果外星人是绿色的，就打印一条消息，指出玩家获得了5个点。
#如果外星人是黄色的，就打印一条消息，指出玩家获得了10个点。
#如果外星人是红色的，就打印一条消息，指出玩家获得了15个点。
alien_color = 'green'
if alien_color == 'green':
    print("U just shoot a alien in green, U got 5 points!")
elif alien_color == 'yellow':
    print("U shoot a alien in yellow, U got 10 points!")
else:
    print("U shoot a red alien,U got 15 points!")
#编写这个程序的三个版本，他们分别在外星人为绿色、黄色、红色时打印一条消息。
alien_color = 'red'
if alien_color == 'green':
    print("U just shoot a alien in green, U got 5 points!")
elif alien_color == 'yellow':
    print("U shoot a alien in yellow, U got 10 points!")
else:
    print("U shoot a red alien,U got 15 points!")

print("\n 简洁代码块版本：")
alien_color = 'red'
if alien_color == 'green':
    point = 5
elif alien_color == 'yellow':
    point = 10
elif alien_color == 'red':
    point = 15
print("U just shoot a alien in "+ alien_color+","+"U got "+str(point)+"!")


#5-6人生的不同各阶段：设置变量age的值，再编写一个if-elif-else结构，根据age的值判断处于人生的哪个阶段。
#如果一个人的年龄小于2岁，就打印一条消息，指出他是婴儿。
#如果一个人的年龄为2岁（含）~4岁，就打印一条消息，指出他正蹒跚学步。
#如果一个人的年龄为4岁（含）~13岁，就打印一条消息，指出他是儿童。
#如果一个人的年龄为13岁（含）~20岁，就打印一条消息，指出他是青少年。
#如果一个人的年龄为20岁（含）~65岁，就打印一条消息，指出他是成年人。
#如果一个人的年龄超过65岁（含），就打印一条消息，指出他是老年人。
print("\n人生的不同各阶段:")

age = 37
if age < 2:
    print("U are a baby!")
elif age < 4:
    print("U are a toddler")
elif age < 13:
    print("U are a children")
elif age < 20:
    print("U are a young man")
elif age < 65:
    print("U are a adult")
elif age >= 65:
    print("U are a old man")



#5-7喜欢的水果：创建一个列表，其中包含你喜欢的水果，再编写一系列独立的if语句，检查列表中是否包含特定的水果。
#将该列表命名为favorite_fruits,并在其中包含三种水果。
#编写5条if语句，每条都检查某种个水果是否包含在列表中，如果包含在列表中，就打印一条消息，如“You really like bananas!".
print("\n最喜欢的水果：")
favorite_fruits=["litchi","watermelon","banana","pear"]

if "litchi" in favorite_fruits:
    print("yes,litchi")
if "watermelon" in favorite_fruits:
    print("yes,watermelon")
if "banana" in favorite_fruits:
    print("yes,banana")
if "pear" in favorite_fruits:
    print("yes,pear")
if "apple" in favorite_fruits:
    print("YES,APPLE")
print("You really like bananas!")

