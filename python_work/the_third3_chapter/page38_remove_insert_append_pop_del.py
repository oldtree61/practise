#3-4嘉宾名单 3-5修改嘉宾名单
dinner_list=['michael','sancy','rachel','buffett','johnson','kiki','kevin','my father','my mother']
print(dinner_list[0].title()+","+dinner_list[1].title()+","+dinner_list[2].title()+","+dinner_list[3].title()+","
      +dinner_list[4].title()+","+dinner_list[5].title()+","+dinner_list[6].title()+","
      +dinner_list[7]+" and "+dinner_list[8]+","+"Welcome to my dinner this weekend!!")

print(dinner_list[0]+" "+"can't attend the dinner this weekend.")


cant_attend=dinner_list[0]
print(cant_attend+" "+"can't attend the dinner this weekend.")

dinner_list[0]='oldtree'
print(dinner_list)
print(dinner_list[0].title()+","+dinner_list[1].title()+","+dinner_list[2].title()+","+dinner_list[3].title()+","
      +dinner_list[4].title()+","+dinner_list[5].title()+","+dinner_list[6].title()+","
      +dinner_list[7]+" and "+dinner_list[8]+","+"Welcome to my dinner this weekend!!")

#3-6添加嘉宾
print(dinner_list[0].title()+","+dinner_list[1].title()+","+dinner_list[2].title()+","+dinner_list[3].title()+","
      +dinner_list[4].title()+","+dinner_list[5].title()+","+dinner_list[6].title()+","
      +dinner_list[7]+" and "+dinner_list[8]+","+"I found a bigger table!!")

dinner_list.insert(0,"bob_at_first")
dinner_list.insert(4,"new_comer_in_middle")
dinner_list.append("punk_at_last")
print(dinner_list)
message=(dinner_list[0].title()+","+dinner_list[1].title()+","+dinner_list[2].title()+","+dinner_list[3].title()+","
      +dinner_list[4].title()+","+dinner_list[5].title()+","+dinner_list[6].title()+","
      +dinner_list[7]+" and "+dinner_list[8]+","+dinner_list[9].title()+","+dinner_list[10].title()+","+dinner_list[-1].title()
         +","+"Welcome to my dinner this weekend!")
print(message)

#3-7缩减名单：

message=(dinner_list[0].title()+","+dinner_list[1].title()+","+dinner_list[2].title()+","+dinner_list[3].title()+","
      +dinner_list[4].title()+","+dinner_list[5].title()+","+dinner_list[6].title()+","
      +dinner_list[7]+" and "+dinner_list[8]+","+dinner_list[9].title()+","+dinner_list[10].title()+","+dinner_list[-1].title()
         +","+"Welcome to my dinner this weekend!!Oh,I am very sorry to told all of u guys,I have to invite just two person "
              "to my dinner cause my new table did't arrive yet")
print(message)
guest_pop1=dinner_list.pop(0)
print(guest_pop1.title()+","+"I am very sorry that I can't invite you to my dinner.")

guest_pop2=dinner_list.pop(3)
print(guest_pop2.title()+","+"I am very sorry that I can't invite you to my dinner.")

guest_pop3=dinner_list.pop(4)
print(guest_pop3.title()+","+"I am very sorry that I can't invite you to my dinner.")

guest_pop4=dinner_list.pop(5)
print(guest_pop4.title()+","+"I am very sorry that I can't invite you to my dinner.")

guest_pop5=dinner_list.pop(6)
print(guest_pop5.title()+","+"I am very sorry that I can't invite you to my dinner.")

print(dinner_list)
guest_pop6=dinner_list.pop(2)
guest_pop7=dinner_list.pop(2)
guest_pop8=dinner_list.pop(2)
guest_pop9=dinner_list.pop(2)
guest_pop10=dinner_list.pop(2)
print(guest_pop6.title()+","+"I am very sorry that I can't invite you to my dinner.")
print(guest_pop7.title()+","+"I am very sorry that I can't invite you to my dinner.")
print(guest_pop8.title()+","+"I am very sorry that I can't invite you to my dinner.")
print(guest_pop9.title()+","+"I am very sorry that I can't invite you to my dinner.")
print(guest_pop10.title()+","+"I am very sorry that I can't invite you to my dinner.")

print(dinner_list)

print(dinner_list[0].title()+","+"You're still on my dinner list")
print(dinner_list[1].title()+","+"You're still on my dinner list")

del dinner_list[0]
del dinner_list[0]
print(dinner_list)

#my hope
new_dinner_list=["oldtree","sancy"]
print(new_dinner_list[1].title()+","+"just you and Daddy to have dinner together,my daughter")
