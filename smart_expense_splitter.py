print("Welcome to the Smart Expense Splitter!")


#taking user input for total budget, total bill.
total_buget = float(input("Enter the total budget ready to spend: "))
total_bill = float(input("Enter the total bill amount: "))


#taking user input for number of people and validating it.
num_people = int(input("Enter the number of people: "))
if num_people <= 0:
    print("Number of people must be greater than zero.Thank you!")
    exit()
elif num_people == 1:
    print("Only one person is paying the bill. No need to split. Thank you!")
    exit()


#taking each person's name and validating it.
names = []
for i in range(1,num_people+1):
    names.append(input(f"Enter person {i} name :"))
print("The persons are :",names)


#asking whether single paid or multiple paid:
while True:
    ask = input("Does bill is paid by multiple person.(yes/no)?").lower()
    if  "yes" in ask:
        n1 = int(input(f"How many paid the bill out of {num_people} :"))
        if n1 == 0 or n1 > num_people:
            print(f"number of people i.e, {num_people} is lesser than or greater the number of people who are paying bill i.e,{n1} \n Please check once:")
            continue
        elif n1 == 1 :
            print("it's paid by single person \n if you entered wrong,please correct it")
            continue
        else:
            print(f"needs to be updated..:")
            break

    elif  "no" in ask :
             print("The Bill is paid by single person.....!")
             break
    else:
        print("Invalid input say.(yes/no)?")

#discount application:
discount_percentage = float(input("Enter the discount percentage (if any, otherwise enter 0): "))
if discount_percentage > 0:
    discount_amount = total_bill * (discount_percentage / 100)
    total_bill -= discount_amount
    print(f"Discount amount: {discount_amount}")
elif discount_percentage < 0:
    print("Invalid discount percentage. It cannot be negative. Thank you!")
    exit()
elif discount_percentage ==100:
    total_bill = 0
    print("Total bill after discount: 0")
elif discount_percentage > 100:
    print("Invalid discount percentage. It cannot be greater than 100. Thank you!")
    exit()
else:
    print("No discount applied.")
print(f"Total bill amount after discount (if any): {total_bill}")


#tip suggestion:
tip_percentage = 0
tip_suggestion = input("Do you want any tip suggestions? (yes/no): ").lower()
if  "yes" in tip_suggestion:
    if total_bill < 500:
        print("no need to tip, but you can round up the bill to the nearest 10 or 50 for convenience.")
        suggested_tip = 0
    elif 500 <= total_bill < 1000:
        print("A tip of 3% is suggested for good service.")
        suggested_tip = 3
    elif 1000 <= total_bill < 5000:
        print("A tip of 5% is suggested for good service.")
        suggested_tip = 5
    elif 5000 <= total_bill < 10000:
        print("A tip of 8% is suggested for good service.")
        suggested_tip = 8
    else:
        print("A tip of 20% is suggested for good service.")
        suggested_tip = 20
    print(f"Suggested tip amount: {suggested_tip}%")

    confirm = input("Is the suggested tip percentage acceptable? (yes/no): ").lower()
    if "yes" in confirm:
        tip_percentage = suggested_tip
        print(f"Tip percentage set to: {tip_percentage}%")
        print(f"Tip amount based on suggested percentage: {total_bill * (tip_percentage / 100)}")
        print(f"Total bill including tip: {total_bill + (total_bill * (tip_percentage / 100))}")
    else:
        tip_percentage = float(input("Enter your desired tip percentage: "))
else:
    tip_percentage = float(input("Enter the tip percentage (e.g., 15 for 15%): "))
paid_by = input("Enter the name of the person who paid the bill: ")
tip_amount = total_bill * (tip_percentage / 100)
final_bill = total_bill + tip_amount
per_person = final_bill/num_people
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
#I can also print it as //{print(f"Total bill including tip: ₹{final_bill:.2f}")}\\ 
# here f is format specifier and .2f is for 2 decimal places.
#ctrl+alt+4 = ₹
print("Each person should pay:", per_person)
print("Bill paid by:", paid_by,":" ,final_bill)
print("Each person should pay:", per_person,"for", paid_by),print(" (except", paid_by, "who paid the full amount)")
print("Thank you!\nHave a great day!")
