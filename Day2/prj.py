print("Welcome to the tip calculator\n")
bill=input("What was the total bill? $")
tip_percent=input("What percentage tip would you like to give? 10, 12 or 15? ")
people=input("How many people to split the bill? ")

tip=float(bill)/100*float(tip_percent)

total_bill=float(bill)+float(tip)

split=total_bill/float(people)

print("Each person should pay: $" + str(round(split, 2)))

