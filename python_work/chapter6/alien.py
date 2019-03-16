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