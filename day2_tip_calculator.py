print("Welcome to Tip Calculator")
amount = float(input("What was your total bill? $"))
percentage = int(input("What percentage of tip would you like 10, 12 or 15? "))
people = int(input("How many people are splitting the bill? "))

total = ((amount+((percentage/100)*amount))/people)
new_total = "{:.2f}".format(total)

print(f"Each person should pay ${new_total}")
