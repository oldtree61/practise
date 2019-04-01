#6-7 人：在为完成练习6-1而编写的程序中，再创建两个表示人的字典，然后将这三个字典都存储在一个名为people的列表中。遍历这个
#列表，将其中每个人的所有信息都打印出来。
print("6-7 人：在为完成练习6-1而编写的程序中，再创建两个表示人的字典，然后将这三个字典都存储在一个名为people的列表中。遍历这个列表，将其中每个人的所有信息都打印出来")

people = []
people1 = {'first_name':'oldtree',
            'last_name':'liu',
            'age':37,
            'city':'virginia',
          }
people.append(people1)

people2 = {'first_name':'rainie',
            'last_name':'jie',
            'age':26,
            'city':'japan',
          }
people.append(people2)

people3 = {'first_name':'kiki',
            'last_name':'si',
            'age':23,
            'city':'china',
          }
people.append(people3)


for people_info in people:
    name = people_info['first_name'].title() + " " + people_info['last_name'].title()
    age = people_info['age']
    city = people_info['city']
    print(name + " is " + str(age) + " years old," + "live in " + city + ".")


#6-8 宠物：创建多个字典，对于每个字典，都是用一个宠物的名称来给他命名；在每个字典中，包含宠物的类型及其主人的名字。
#将这些字典存储在一个名为pets的列表中，再遍历该列表，并将宠物的所有信息都打印出来。
print("\n6-8 宠物：")
pets = []
cats = {'type': 'cat',
        'owner': 'kiki',
        'name': 'shabi'}
pets.append(cats)

dogs = {'type': 'dog',
        'owner': 'rainie',
        'name': 'rita'}
pets.append(dogs)

turtles = {'type': 'turtles',
        'owner': 'oldtree',
        'name': 'billy'
           }
pets.append(turtles)

for pet in pets:
    type = pet['type']
    owner = pet['owner']
    name = pet['name']
    print(name.title() +  " is a " + type + " which belongs to " + owner)
    

#6-9:喜欢的地方：创建一个名为favorite_places的字典。在这个字典中，将三个人的名字用作键；对于其中的每个人，都存储他喜欢的1~3个
#地方。为让这个练习更有趣些，可让一些朋友指出他们喜欢的几个地方。遍历这个字典，并将其中每个人的名字及其喜欢的地方打印出来。
print("\n6-9:喜欢的地方：")

favorite_places = {'rainie':['japan','thailand','switzerland'],
                   'oldtree':['thailand','united states'],
                   'sancy':['united states',],
                   }
for name , place in favorite_places.items():
    print(name.title() + "'s favorite place is:")
    for favorite_place in place:
        print("\t" + favorite_place.title())


#6-10喜欢的数字：修改为完成练习6-2而编写的程序，让每个人都可以有多个喜欢的数字，然后将每个人的名字及其喜欢的数字打印出来。
print("\n6-10喜欢的数字：")

favorite_numbers = {'sancy': [1,21,9],
                   'oldtree': [6,9,20],
                   'michael':[8,2,18],
                   'linda': [5,9],
                   'kiki': [16,6,],
                   }
for name , numbers in favorite_numbers.items():
    print(name.title() + "'s favorite numbers are:")
    for number in numbers:
        print("\t" + str(number))


#6-11 城市：创建一个名为cities的字典，其中将三个城市名用作键；对于每座城市，都创建一个字典，并在其中包含该城市所属的国家、人口
#约数以及一个有关该城市的事实。在表示每座城市的字典中，应包含country、population和fact等键。将每座城市的名字以及有关他们的信息都
#打印出来。

print("\n6-11城市：")

cities = {
          'bangkok': {'country': 'thailand',
                      'population': 5000000,
                      'fact': 'The most famouse travel place.',
                      },  #注意各值字典也要用逗号“，”相隔
          'virginia': {'country': 'the united states',
                       'population': 1600000,
                       'fact': 'The place which is my destination in my rest of my life I live in.',
                       }, #注意各值字典也要用逗号“，”相隔
          'NN': {'country': 'china',
                 'population': 4800000,
                 'fact': 'The place which I struggle with,even I borned here. ',
                 },       #注意各值字典也要用逗号“，”相隔
          }
for city , info in cities.items():
    print(city.title() +
          " is a city in " +
          info['country'] +
          ", the population is " +
          str(info['population']) +
          ",the fact is:" +
          info['fact'])


#6-12 扩展：本章的示例足够复杂，可以以很多方式进行扩展了。请对本章的一个示例进行扩展；添加键和值、调整程序要解决的问题或改进
#输出格式。
print("\n6-12扩展：")

