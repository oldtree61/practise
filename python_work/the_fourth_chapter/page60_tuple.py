#4-13自助餐： 有一家自助式餐馆，只提供五种简单的食品。请想出五种简单的食品，并将其储存在一个元组中。
foods=("chicken","fruits","rice","vegetables")
for food in foods:#使用一个for循环将该餐馆提供的五种食品都打印出来。
    print(food)

 #尝试修改其中一个元素，核实PYTHON确实会拒绝你这样做。
#foods[0]="salad"

print("\n餐馆调整了菜单，替换了它提供的其中两种食品:")
foods=("salad","fruits","milk","vegetables")#餐馆调整了菜单，替换了它提供的其中两种食品。请编写一个这样的代码块，给元组变量赋值，并使用一个for循环将新元组每个元素都打印出来。
for food in foods:
    print(food)