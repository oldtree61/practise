#7.2.4使用break退出循环
prompt = "\nPlease enter the name of city you have visited: "
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print("I'd love to go to "+ city.title() + "!")
