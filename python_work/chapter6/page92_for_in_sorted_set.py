#6-4词汇表2：既然你知道了如何遍历字典，现在请整理你为完成练习6-3而编写的代码，将其中的一系列print语句替换为一个遍历字典中的键
#和值得循环。确定该循环正确无误后，再在词汇表中添加5个Python术语。当你再次运行这个程序时，这些新术语及其含义将自动包含在输出中。
print("\n6-4词汇表2：")
words_dictionary = {'function': '功能，函数',
                    'string': '字符串',
                    'variable': '变量',
                    'print': '打印',
                    'interge': '整数',
                    }
words_dictionary['for in'] = '遍历'
for key , value in words_dictionary.items():
    print(key + ":" + value)

#6-5河流：创建一个字典，在其中存储三条大河流及其流经的国家。其中一个键-值对可能是‘nile':'egypt'.

print("\n6-5河流:")

rivers = {'nile':'egypt',
          'yangtze river':'china',
          'amazon river':'brazil',
          }
for river,country in rivers.items():       #使用循环为每条河流打印一条消息，如“The nile runs through Egypt."
    print("The " + river.title() +" runs through "+ country.title())

#使用循环将该字典中的每条河流的名字都打印出来。
print("\n使用循环将该字典中的每条河流的名字都打印出来:")
rivers = {'nile':'egypt',
          'yangtze river':'china',
          'amazon river':'brazil',
          }
for river in rivers.keys():
    print(river.title())

#使用循环将该字典包含的每个国家的名字都打印出来。
print("\n使用循环将该字典包含的每个国家的名字都打印出来:")
rivers = {'nile':'egypt',
          'yangtze river':'china',
          'amazon river':'brazil',
          }
for country in rivers.values():
    print(country.title())

#6-6调查：在6.3.1节编写的程序favorite_languages.py中执行以下操作。
print("\n6-6调查:")
#创建一个应该会接受调查的人员名单，其中有些人已包含在字典中，而其他人未包含在字典中。

favorite_language = {'jen':'python',
                     'sarah':'c',
                     'edward':'ruby',
                     'phil':'python',
                     }

others = ['oldtree','sancy','phil','sarah']

for name in others:          #遍历这个人员名单，对于已参与调查的人，打印一条消息表示感谢。对于还未参与调查的人，打印一条消息邀请他参与调查。
    if name in favorite_language.keys():
       print(name.title() + ",thank you for your research.")
    else:
        print(name.title() + ",you are invited to participate in the survey.")



