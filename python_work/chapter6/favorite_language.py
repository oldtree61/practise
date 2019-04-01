#遍历字典：遍历所有键-值对
print("6.3遍历字典：遍历所有键-值对")

favorite_language = {'jen':'python',
                     'sarah':'c',
                     'edward':'ruby',
                     'phil':'python',
                     }
for name,language in favorite_language.items():
    print(name.title()+":"+language.title())


#6.3.2遍历字典中的所有键
print("\n遍历字典中的所有键：")

favorite_language = {'jen':'python',
                     'sarah':'c',
                     'edward':'ruby',
                     'phil':'python',
                     }
for name in favorite_language.keys():
    print(name.title())


#可使用当前键来访问预支相关联的值：
print("\n可使用当前键来访问预支相关联的值:")

favorite_language = {'jen':'python',
                     'sarah':'c',
                     'edward':'ruby',
                     'phil':'python',
                     }
friends = ['phil', 'sarah']
for name in favorite_language.keys():
    print(name.title())

    if name in friends:  #此行的if语句一定要在循环for语句后空格，否则无法依次检查列表friends列表是否在字典favorite_language里
       print("Hi " + name.title() +
          ",I see your favorite language is "+
          favorite_language[name].title()+
          "!")
if 'erin'not in favorite_language.keys():
    print("Erin,please take our poll!")


#6.3.3按顺序遍历字典中的所有键
print("\n按顺序遍历字典中的所有键:")

favorite_language = {'jen':'python',
                     'sarah':'c',
                     'edward':'ruby',
                     'phil':'python',
                     }
for name in sorted(favorite_language.keys()):
    print(name.title() +",thank you for taking the poll.")

#6.3.4遍历字典中的所有值：
print("\n遍历字典中的所有值：")

favorite_language = {'jen':'python',
                     'sarah':'c',
                     'edward':'ruby',
                     'phil':'python',
                     }
print("The following languages have been mentioned:")
for language in favorite_language.values():
    print(language.title())

#集合：为剔除值的重复项，可使用集合（set）.集合类似于列表，但每个元素都必须是独一无二的：

print("\n集合set:")

favorite_language = {'jen':'python',
                     'sarah':'c',
                     'edward':'ruby',
                     'phil':'python',
                     }
for language in set(favorite_language.values()):
    print(language.title())

