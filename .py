print("Who paid the bill?")
paid_by = []
names = ["vikas","ullas","sachin","santosh"]
n1 = 2
print("Number     Name")
for i in range(len(names)):
    print(f" \n{i+1}. \t  {names[i]}")
for k in range(1, n1+1):
    payer = int(input("Enter person number by reffering above,that paid the bill: "))
    paid_by.append(names[payer-1])
print(f"{paid_by} paid the bill")