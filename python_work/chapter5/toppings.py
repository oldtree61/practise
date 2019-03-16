
#如果比萨店里的青椒用完了，可在for循环中包含一条if语句
print("\n如果比萨店里的青椒用完了，可在for循环中包含一条if语句:")
requested_toppings = ["mushrooms","green peppers","extra cheese"]
for requested_topping in requested_toppings:
    if requested_topping == "green peppers":
        print("Sorry,we are out of green peppers right now.")
    else:
        print("Adding "+requested_topping+".")
print("\nFinishing making your pizza!")




#确定列表不是空的
print("\n检查是否列表为空:")
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding "+ requested_topping+".")
    print("\nFinishing making your pizza!")
else:
        print("Are you sure you want a plain pizza?")

#5.4.3使用多个列表
print("\n使用多个列表:")

available_toppings = ["mushrooms","olives","green peppers","pepperoni","pineapple","extra cheese"]
requested_toppings = ["mushrooms","french fries","extra cheese"]
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding "+ requested_topping+".")
    else:
        print("Sorry,we don't have "+requested_topping+".")
print("\nFinishing making your pizza!")