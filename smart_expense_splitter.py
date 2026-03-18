total_bill = float(input("Enter the total bill amount: "))
num_people = int(input("Enter the number of people: "))
tip_percentage = float(input("Enter the tip percentage (e.g., 15 for 15%): "))
paid_by = input("Enter the name of the person who paid the bill: ")
tip_amount = total_bill * (tip_percentage / 100)
final_bill = total_bill + tip_amount
per_person = final_bill/num_people
print("\n--- Bill Summary ---")
print("Total bill including tip:", final_bill)
#I can also print it as //{print(f"Total bill including tip: ₹{final_bill:.2f}")}\\ 
# here f is format specifier and .2f is for 2 decimal places.
#ctrl+alt+4 = ₹
print("Each person should pay:", per_person)
print("Bill paid by:", paid_by,":" ,final_bill)
print("Each person should pay:", per_person,"for", paid_by),print(" (except", paid_by, "who paid the full amount)")
print("Thank you!\nHave a great day!")
