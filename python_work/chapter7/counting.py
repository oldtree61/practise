
#7.2.1 使用while循环

current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

#7.2.5在循环中使用continue 从1到10，只打印其中的奇数的循环
print("\n#7.2.5在循环中使用continue 从1到10，只打印其中的奇数的循环")

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)


#7.2.6避免无限循环
print("\n#7.2.6避免无限循环")
x = 1
while x <= 5:
    print(x)
    x += 1


