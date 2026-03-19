total_buget = float(input("Enter your total budget which you are willing to spend: "))
total_bill = float(input("Enter the total bill amount: "))
num_people = int(input("Enter the number of people: "))
if num_people <= 0:
    print("Number of people must be greater than zero.Thank you!")
    exit()
elif num_people == 1:
    print("Only one person is paying the bill. No need to split. Thank you!")
    exit()
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
if tip_suggestion == "yes":
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
    if confirm == "yes":
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
if final_bill > total_buget:
    print("Warning: The total bill including tip exceeds your budget!\n\n")
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
