#7.3.3使用用户输入来填充字典
responses = {}
polling_active = True  #设置一个标志，指出调查是否继续

while polling_active:
    name = input("\nWhat is your name? ")
    response = input("\nWhich mountain would you like to climb someday? ")

    responses[name] = response #将用户输入的人名和想爬的山储存到字典中!!!!!

    repeat = input("\nWould you like to let another person respond?(yes/no) ")
    if repeat == 'no':          #注意if语句中判断是==，后面要加：
       polling_active = False   #注意if语句下一行要缩进

print("--Poll Result--")
for name , response in responses.items():
    print(name + " would like to climb " + response + ".")

print(responses)




