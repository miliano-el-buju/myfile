print("This program checks if you are eligible for the a bank loan or not")

salary=int(input("how much is your salary: \n "))
if(salary>1000):
    amount=200
    print("You are eligible to get a bank loan by paying $ ",amount, "monthly")
    
elif(salary==1000):
        amount=500
        print("You are eligible to get bank loan with higher monthly price$",amount,"monthly")
else:
    print("sorry you are not eligible")
            