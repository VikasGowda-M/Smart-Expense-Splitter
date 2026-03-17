total_bill = float(input("Enter the total bill amount: "))
num_people = int(input("Enter the number of people splitting the bill: "))
tip_percentage = float(input("Enter the tip percentage (e.g., 15 for 15%): "))
tip_amount = total_bill * (tip_percentage / 100)
final_bill = total_bill + tip_amount
per_person = final_bill/num_people
print("Total bill including tip:", final_bill)
print("Each person should pay:", per_person)
