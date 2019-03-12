#根据年龄段收费的游乐场：
age = 12
if age<4:
    print("Your admission cost is $0.")
elif age< 18:
    print("Your admission cost is $5.")
else:
    print("Your admission cost is $10.")

#以上案例的另一种简洁代码块表达方式：

age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10
print("Your admission cost is $"+str(price)+".")


#下面假设对于65岁（含）以上的老人，可以半价（即5美元）购买门票：可使用多个elif代码块

age = 58
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
else:
    price = 5

print("Your admission cost is $"+str(price)+".")