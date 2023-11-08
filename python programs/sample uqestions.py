age = int(input("enter your age:   "))
if age>=18:
    print("vote eligible")
else:
    print("Not Eligiblle")    

#2dn sample
num = int(input("enter your number:  "))
if num%2 ==0:
    print("even")
else: 
    print("odd")

    #3rd sample
    num = int(input("enter the number:   "))
    if num%7 ==0:
        print("dividable")
    else: 
        print("not dividable")

        #4 sample
    num = int(input("Enter you Number:  "))
    if num%5==0:
        print("yes")
    else:
        print("no")    


#5th sample
num = int(input("enter the percentage :   "))
if num>90:
    print("grade A")
if  num>80 and num <=90:
    print("grade b")
if num >=60 and num <=80:
    print("grade c")
if num <60:
    print("failure")

#6th sample

          
cost_price = int(input("enter the bike price:  "))
tax = 0
if cost_price>100000:
    tax = 15/100*cost_price
elif cost_price>50000 and cost_price<=100000:
    tax = 10/100*cost_price
else: 
    tax = 5/100*cost_price
    print("tax will be as follows", tax)

    #7th problem sample
    num = int(input("enetr nay number betweenfrom 1-7 :  "))
    if num ==1:
        print("sunday")
    if num ==2:
        print("monday")
    if num ==3:
        print("tuesday")
    if num ==4:
        print("wednesday")
    if num ==5:
        print("thrusday")
    if num ==6:
        print("friday")
    if num ==7:
        print("saturday")
    else:
        print("bye")    

        # 8 th sample
num1 = input("enter any number: ")
length = len(num1)
if length != 3:
    print("fixed 3 digit number")
else:
    print("not fixed dig")    

    