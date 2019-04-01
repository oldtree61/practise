#6.1一个简单的字典
print("\n1.")
alien_0 = {'color':'green','points':5}

print(alien_0['color'])
print(alien_0['points'])

print("\n2.")
alien_0 = {'color':'green','points':5}
new_points = alien_0['points']
print("You earn "+str(new_points)+" points!")
print("You earn "+str(alien_0['points'])+" points!")


print("\nBig monster:")
big_monster = {'color':'yellow','points':15}
print(big_monster['color'])
print(big_monster['points'])

print("\n6.2.2:")
alien_0 = {'color':'green','points':5}
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)


print("\n6.2.3")
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)


print("\n6.2.4:")
alien_0 = {'color':'green'}
print("The alien is "+alien_0['color']+".")

alien_0['color'] = 'yellow'
print("The ailen is now "+alien_0['color']+".")



print("\n一个有趣的列子:")
#一个有趣的列子，对一个能以不同速度移动的外星人的位置进行跟踪。为此，我们将存储该外星人的当前速度，并据此确定该外星人将向右移动多远：
alien_0 = {'x_position':0,'y_position':25,'speed':'medium'}
print("Original x-position: "+str(alien_0['x_position']))

#向右移动外星人
#根据外星人当前速度决定将其移动多远
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x-position: "+str(alien_0['x_position']))

alien_0['speed'] = 'fast'
print(alien_0)

new_position = alien_0['x_position'] + x_increment
print("New position :"+str(new_position))


#由类似对象组成的字典：
print("\n由类似对象组成的字典：")

favorite_languages = {'sancy':'python',
                      'oldtree':'python',
                      'michael':'c',
                      'manson':'java',
                      }
print("Oldtree favorite language is "+
      favorite_languages['oldtree']+
      ".")


#6.4嵌套
print("\n\n6.4嵌套")
#6.4.1字典列表：
print("\n6.4.1字典列表")
alien_0 = {'color':'green','points':5}
alien_1 = {'color':'yellow','points':10}
alien_2 = {'color':'red','points':15}

aliens = [alien_0,alien_1,alien_2]
for alien in aliens:
    print(alien)

#使用range（）自动生成外星人，床架一个用于存储外星人的空列表
print("\n使用range（）自动生成外星人，创建一个用于存储外星人的空列表：")

aliens = []

for alien_number in range(30):    #创建30个绿色的外星人
    new_alien = {'color':'green', 'points':5, 'speed':'slow'}
    aliens.append(new_alien)

for alien in aliens[:5]: #显示前5个外星人,使用了一个切片来打印前5个外星人
    print(alien)
print("...")

print("Total number of aliens:" + str(len(aliens))) #显示创建了多少个外星人
print(len(aliens))

#要将前三个外星人修改成为黄色、速度为中等且值10个点，你可以这样做：
#创建一个用于存储外星人的空列表
#创建30个绿色的外星人
#将前3个外星人改成黄色，速度为中且值10个点
#显示前5个外星人
print("\n#要将前三个外星人修改成为黄色、速度为中等且值10个点，你可以这样做：")

aliens = []
for alien_number in range(0,30):  #@@@@@注意这里是in range，不是in aliens,因为要用range()函数来创建数量为30个的外星人！
    new_alien = {'color':'green', 'points':5, 'speed':'slow'}
    aliens.append(new_alien)

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'
for alien in aliens:
        print(alien)

print("\n")
for alien in aliens:
    if alien['color']  =='yellow':
       alien['color'] ='red'
       alien['points'] = 15
       alien['speed'] = 'fast'

    print(alien)

print(".....")



aliens = []

for new_alien in range(30):    #创建30个绿色的外星人
    new_alien = {'color':'green', 'points':5, 'speed':'slow'}
    aliens.append(new_alien)

for alien in aliens[:5]: #显示前5个外星人,使用了一个切片来打印前5个外星人
    print(alien)
print("...")
