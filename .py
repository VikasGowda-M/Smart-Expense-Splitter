num_people = 6
names =["vik","pri","ull","kar","kish","pre"]
# n1 = 2
# paid_by = ["vik","pri"]
total_bill = 8000
final_bill=8000
per_person = final_bill/num_people
records = []
total_buget=7000
tip_amount=3000
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
                    payer = int(input(f"Enter person number ({k}) by reffering above,that paid the bill: "))
                    if 1 <= payer <= num_people:
                        if names[payer-1] in paid_by:
                                  print(f"{names[payer-1]} already added to the list of people who paid the bill. Please choose a different person.")
                        else:
                                paid_by.append(names[payer-1])
                                break
                    else:
                        print("enter valid input,your value doesn't match the number of names given: ")
            
            while True :
                
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
    print("perperson:", per_person)
    not_paid = []
    for payers in names:
        if payers not in paid_by:
            not_paid.append(payers)
    print("not paid", not_paid)
    num_not_paid=len(not_paid)
    print("noof people not paid:", num_not_paid)


    # records =[('vik', 6000), ('pri', 2000)]
    amounts={}
    for name,amt in records:
        amounts[name]=amt
        print(f"{name} paid : {amt}")
    balance={}
    for name in names:
        paid = amounts.get(name,0)
        balance[name]=paid - per_person
    print("the Balance List is", balance)
    print("\n--- Bill Summary ---\n")

#comparing total budget with final bill:
    if final_bill > total_buget:
        print("Warning: The total bill including tip exceeds your budget!\n")
    elif final_bill < total_buget:
        print("The total bill including tip is within your budget.\n")
    else:
        print("The total bill including tip exactly matches your budget.\n")
        
    per_person = final_bill/num_people
    print("Total bill amount excluding tip:", total_bill)
    print("Tip amount:", tip_amount)
    print("Total bill including tip:", final_bill)
    creditors = []
    debitors=[]
    for name,amt in balance.items():
        if amt > 0:
            creditors.append([name,amt])
        elif amt<0:
            debitors.append([name,-amt])
    print("------settelments--------")

    for d in debitors:
        for c in creditors:
            if d[1] == 0:
                break
            pay = min(d[1],c[1])

            print(f"{d[0]} should  pay {pay:.2f} to {c[0]}")
            d[1] -= pay
            c[1] -= pay






# print("perperson:", per_person)
# not_paid = []
# for payers in names:
#     if payers not in paid_by:
#         not_paid.append(payers)
# print("not paid", not_paid)
# num_not_paid=len(not_paid)
# print("noof people not paid:", num_not_paid)


# # records =[('vik', 6000), ('pri', 2000)]
# amounts={}
# for name,amt in records:
#     amounts[name]=amt
#     print(f"{name} paid : {amt}")
# balance={}
# for name in names:
#     paid = amounts.get(name,0)
#     balance[name]=paid - per_person
# print("the Balance List is", balance)
# creditors = []
# debitors=[]
# for name,amt in balance.items():
#     if amt > 0:
#         creditors.append([name,amt])
#     elif amt<0:
#         debitors.append([name,-amt])
# print("------settelments--------")

# for d in debitors:
#     for c in creditors:
#         if d[1] == 0:
#             break
#         pay = min(d[1],c[1])

#         print(f"{d[0]} should  pay {pay:.2f} to {c[0]}")
#         d[1] -= pay
#         c[1] -= pay





