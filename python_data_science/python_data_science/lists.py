#list go
list1 = [1,2,3,4,5,6,[2,3,4,2,233]]
list2 = ['d','g','n','o']
list3 = ["kush", "mukund","kunal",1,3]
print("list of numebr will be as:- {}".format(list1))

# print("item popped by me is:-",list.pop())
print(list1.pop())
print(list2[0:3])

#checking mutability
list1[0]= 12
print(list1)