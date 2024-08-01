print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15?"))
split = int(input("How many people to split the bill?"))
total = bill*(tip/100)
total_new = total + bill
split_new = total_new/split
new_total = "{:.2f}".format(split_new)
new_bill = str(new_total)
print(f"Each person should pay: ${new_bill}")