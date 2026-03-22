total_bill = 0
while True:
    money = input("Do you want to add the expense or will you enter the total_bill,(yes/no)? :")
    if "yes" in money:
        expenses = []
        how_many = input("Enter the number of items or products or food purchased or (done):")
        while True:            
            if how_many == 0:
                print("your total bill is 0 ")
                exit()
            elif "done" in how_many:
                break
            else:
                how_many = int(how_many)               
                for v in range(1,how_many+1):
                    amt = int(input(f"expense of {v} :"))
                    expenses.append(float(amt))
                break
        print("All expenses :",expenses)
        print("total_bill is :",sum(expenses))
        total_bill = sum(expenses)           
        break
    elif "no" in money:
        total_bill = input("enter the total_bill :")
        break
    else:
        print("invalid input ....")

        