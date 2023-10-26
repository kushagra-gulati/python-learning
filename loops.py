from tkinter.messagebox import QUESTION

from numpy import true_divide


for k in range(1,45,5):
    if k%2 == 0:
        print(k,"is even")
    else:
        print(k,"is odd")


#2nd sample


fl = [2.5, 16.42, 10.77, 8.3, 34.21]
count_greater = 0

for num in fl:  
    if num > 10:
        count_greater += 1


print(len(list(filter(lambda n:n>10,fl))))

print(count_greater)

# 3rd sample QUESTION
n = 470
new_list= [11,469]
found = False
for n1 in new_list:
    for n2 in new_list:
        if(n1 + n2 == n):
            found = True
            break
        if found:
            print(n1,n2)
            break