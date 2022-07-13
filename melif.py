print("This program checks the zoo Discounts")
print(", and entrance price is $120 ")

price=120
times=int(input("how many times did  you go to this zoo before\n "))

if (times==3):
    price=120-30
    print("Your total included discountn will be $",price)
    
elif(times==4):
    price=120-50
    print("Your total  included will be $",price)
    
elif(times==5):
    price=120-60
    print("Your total included discount will be $",price)
    
elif(times==6):
    price=120-70
    print("Your total included discount will be $",price) 
    
else:
    print("YOUR TOTAL PRICE IS $",price, "and you are not eligiblefor discount in this  time")
    