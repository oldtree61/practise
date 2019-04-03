#7.3.2删除包含特定值的所有列表元素
#假设你有一个宠物列表，其中包含多个值为‘cat’的元素。要删除所有这些元素，可不断运行一个while循环，直到列表中不再包含值‘cat'

pets = [ 'dog','cat','dog','goldfish','cat','rabbit','cat']
print(pets)

while 'cat'in pets:
    pets.remove('cat')
print(pets)