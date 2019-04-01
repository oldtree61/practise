#7.1.1编写清晰的程序

name = input("please enter your name: ")
print("Hello," + name + "!")


#  +=

prompt = "If you tell us who you are,we can personalize the message you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
print("\nHello," + name + "!")