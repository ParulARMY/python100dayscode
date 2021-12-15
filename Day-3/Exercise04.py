#Pizza Order
print("Welcome to python pizza deliveries!\n")
print("Small pizza prize is $15\n")
print("Medium pizza prize is $20\n")
print("Large pizza prize is $25\n")

size= input("What size pizza do you want? S,M,L\n")
print("pepperoni for small pizza is $2\n")
print("pepperoni for medium and large pizza is $3\n")
add_pepperoni = input("Do you want pepperoni ? Y or N ")
print("Extra cheese for any size pizza for $1\n")
extra_cheese = input("Do you want extra cheese?")
bill=0
if size =="S":
    bill+=15
elif size=="M":
    bill+=20
else:
    bill+=25
if add_pepperoni =='Y':
    if size=='S':
        bill+=2
    else:
        bill+=3
    if extra_cheese=='Y':
        bill+=1
    print(f"Your total bill is {bill}")
