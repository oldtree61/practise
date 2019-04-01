#7.3.1在列表之间移动元素

#首先创建一个待验证用户列表
#和一个用于储存已验证用户的空列表

unconfirmed_users = ['alice','brain','candace']
confirmed_users = []

while unconfirmed_users:   #验证每个用户直到没有未验证用户为止，将每个经过验证的列表都移动到已验证用户列表中
    current_user = unconfirmed_users.pop()
    print("Verifying user:" + current_user.title())
    confirmed_users.append(current_user)

print("\nThe following users have been confirmed:")  #显示所有已验证的用户
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

