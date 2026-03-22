# total_bill = 0
# while True:
#     money = input("Do you want to add the expense or will you enter the total_bill,(yes/no)? :")
#     if "yes" in money:
#         expenses = []
#         how_many = input("Enter the number of items or products or food purchased or (done):")
#         while True:            
#             if how_many == 0:
#                 print("your total bill is 0 ")
#                 exit()
#             elif "done" in how_many:
#                 break
#             else:
#                 how_many = int(how_many)               
#                 for v in range(1,how_many+1):
#                     amt = int(input(f"expense of item or food {v} :"))
#                     expenses.append(float(amt))
#                 break
#         print("All expenses :",expenses)
#         print("total_bill is :",sum(expenses))
#         total_bill = sum(expenses)           
#         break
#     elif "no" in money:
#         total_bill = input("enter the total_bill :")
#         break
#     else:
#         print("invalid input ....")




total_bill = 6000
names = ["vik","pri","kis","kar"]
num_people = 4

while True:
    paid_by = []
    ask = input("Does bill is paid by multiple person.(yes/no)? :").lower()
    if  "yes" in ask:
        n1 = int(input(f"How many paid the bill out of {num_people} :"))
        if n1 == 0 or n1 > num_people:
            print(f"number of people i.e, {num_people} is lesser than or greater the number of people who are paying bill i.e,{n1} \n Please check once:")
            continue
        elif n1 == 1 :
            print("it's paid by single person \n if you entered wrong,please correct it")
            continue
        else:
            #who paid the bill:
            print("Who paid the bill?")
            print("Number     Name")
            for i in range(len(names)):
                print(f" \n{i+1}. \t  {names[i]}")
            for k in range(1,n1+1):
                while True:
                    payer = int(input(f"Enter person number {k} by reffering above,that paid the bill: "))
                    if 1 <= payer <= num_people:
                        if names[payer-1] in paid_by:
                                  print(f"{names[payer-1]} already added to the list of people who paid the bill. Please choose a different person.")
                        else:
                                paid_by.append(names[payer-1])
                                break
                    else:
                        print("enter valid input,your value doesn't match the number of names given: ")
            
            while True :
                records = []
                total_bill2 = 0
                for name in paid_by:
                    amt = int(input(f"Enter expense paid by {name} :"))
                    total_bill2 += amt
                    records.append((name,amt))
                print("Record of person who paid and their expenes",records)
                if total_bill == total_bill2:
                    print(f"the total bill of expense {total_bill} and the amount paid by {records} matches.\n the total bill is :{total_bill} ")
                    break
                else:
                    print(f" total_bill is {total_bill} \n sum of expenses paid by each of {records} \n both doesn't match, try again")
                    exit1 = input(f"if you want to exit ,enter exit ,oryou like to re enter the expenses of {records},enter continue : ")
                    if "continue" in exit1:
                         print("RE ENTER")
                    else:
                        print("TRY FROM FIRST \nEND..")
                        exit()
            break
    elif  "no" in ask :
            print("The Bill is paid by single person.....!")
            paid_by.append(input("Who paid the bill? Please enter the name: "))
            break
    else:
        print("Invalid input say.(yes/no)?")