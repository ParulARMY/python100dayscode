#Tip Calculator

print("welcome to he tip calculator!")
bill = float(input("what was the total bill?$"))
tip = int(input("What is the percentage tip would you like to give? 10,12,15? "))
people = int(input("How many people to split the bill ?"))
amt =(bill*tip/100)+bill
pay = "{:.2f}".format(round(amt/people,2))
print(f"Each person should pay: $ {pay}")