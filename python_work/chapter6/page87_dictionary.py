#6-1人：使用一个字典来存储一个熟人的信息，包括名，姓，年龄和居住的城市。
#该字典应包含键first_name,last_name,age和city。将存储在该字典中的每项信息都打印出来。
print("\n使用一个字典来存储一个熟人的信息，包括名，姓，年龄和居住的城市。")

people_information = {'first_name':'oldtree',
                      'last_name':'liu',
                      'age':37,
                      'city':'virginia',
                      }
print(people_information['first_name'])
print(people_information['last_name'])
print(people_information['age'])
print(people_information['city'])

print(people_information)


#6-2喜欢的数字：使用一个字典来存储一些人喜欢的数字。请想出5个人的名字，并将这些名字用作字典中的键；想出每个人喜欢的一个数字，
#并将这些数字作为值存储在字典中。打印每个人的名字和喜欢的数字。并让这个程序更有趣，通过询问朋友确保数据是真实的。
print("\n喜欢的数字：")

favorite_number = {'sancy':9,
                   'oldtree':6,
                   'michael':8,
                   'linda':5,
                   'kiki':16,
                   }
print("Sancy's favorite number is "+str(favorite_number['sancy']))
print("oldtree's favorite number is "+str(favorite_number['oldtree']))
print("michael's favorite number is "+str(favorite_number['michael']))
print("linda's favorite number is "+str(favorite_number['linda']))
print("kiki's favorite number is "+str(favorite_number['kiki']))

#词汇表：Python字典可用于模拟现实生活中的字典，但为避免混淆，我们将后者成为词汇表。
#想出你在前面学过的5个编程词汇，将它们用作词汇表中的键，并将它们的含义作为值存储在词汇表中。
#以整洁的方式打印每个词汇及其含义。为此，你可以先打印词汇，在它后面加上一个冒号，再打印词汇的含义；也可在一行打印词汇，
#再使用换行符（\n）插入一个空行，然后在下一个行以缩进的方式打印词汇的含义。
print("\n词汇表")
words_dictionary = {}
words_dictionary['function'] = '功能，函数'
words_dictionary['string'] = '字符串'
words_dictionary['variable'] = '变量'
words_dictionary['print'] = '打印'
words_dictionary['interge'] = '整数'
print(words_dictionary)

print("fuctiong:\n"+words_dictionary['function'])
print("\nstring:\n"+words_dictionary['string'])
print("\nvariable:\n"+words_dictionary['variable'])
print("\nprint:\n"+words_dictionary['print'])
print("\ninterge:\n"+words_dictionary['interge'])


