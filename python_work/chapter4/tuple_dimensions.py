
#元组：不可变得列表成为元组，不可修改的值成为不可变的

dimensions=(200,50)
print(dimensions[0])
print(dimensions[1])


for dimension in dimensions:
    print(dimension)

print("\n")
dimensions=(200,50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions=(400,100)
print("\nMotified dimensions:")
for dimension in dimensions:
    print(dimension)
