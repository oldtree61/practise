
#6.4.2在字典中存储列表：
#存储所点的pizza信息
pizza = {'crust': 'thick',#pizza的外皮类型，下面是配料类型
         'toppings':['mushrooms','extra cheese'],
         }

#概述所点的pizza
print("You ordered a " + pizza['crust'] + "-crust pizza" + "with the following toppings:")

for topping in pizza['toppings']:
    print("\t" + topping)


#每当需要在字典中将一个键关联到多个值时，都可以在字典中嵌套一个列表。
print("\n每当需要在字典中将一个键关联到多个值时，都可以在字典中嵌套一个列表:")

favorite_language = {'jen': ['python','ruby'],
                     'sarah': ['c'],
                     'edward': ['ruby','go'],
                     'phil': ['python','haskell'],
                     }
for name , languages in favorite_language.items():
    print("\n" + name.title() + "'s favorite languages are:")
    for language in languages:
        print("\t" + language.title())
    print("\t" + str(len(languages)))  #确定每个人喜欢的编程语言有几个


#加入if语句的版本
print("\n加入if语句的版本:")

favorite_language = {'jen': ['python','ruby'],
                     'sarah': ['c'],
                     'edward': ['ruby','go'],
                     'phil': ['python','haskell'],
                     }

for name , languages in favorite_language.items():
    if len(languages) <= 1:
        for language1 in languages:
            print("\n" + name.title() + "'s favorite language is " + language1.title())
    else:
        print("\n" + name.title() + "'s favorite languages are:")
        for language in languages:
            print("\t" + language.title())