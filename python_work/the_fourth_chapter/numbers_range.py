print("\n打印1-5的数：")
for value in range(1,6):
    print(value)

print("\n创建一个1-8数字的列表：")
numbers=list(range(1,9))
print(numbers)

print("\n打印1-10中的偶数：")
even_numbers=list(range(2,11,2))
print(even_numbers)


print("\n创建1-10的平方的列表：")
squares=[]
for value in range(1,11):
    square=value**2
    squares.append(square)
print(squares)

#以下代码也可行
squares=[]
for value in range(1,11):
    squares.append(value**2)
print(squares)


digits=list(range(1,11))
print(digits)

digits=[1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))



print("\n创建1-10的平方的列表：")
squares=[]
for value in range(1,11):
    square=value**2
    squares.append(square)
print(squares)

#以下代码也可行
squares=[]
for value in range(1,11):
    squares.append(value**2)
print(squares)
#列表解析
print("以下是列表解析，用一行代码即可：")
squares =[value**2 for value in range(1,11)]
print(squares)

