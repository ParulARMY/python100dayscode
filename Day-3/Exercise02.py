#This program is upgrade version of previous bmi exercise
height = float(input("Enter your height in meters\n"))
weight = float(input("Enter your weight in kgs\n"))
bmi = round(weight/(height*height))
if bmi<18.5:
    print(f"your bmi is {bmi}, you are underweight")
elif bmi<25:
    print(f"your bmi is {bmi}, you have normal weight")
elif bmi<30:
    print(f"your bmi is {bmi}, you are overweight")
elif bmi<35:
    print(f"your bmi is {bmi}, you are obese")
else:
    print("you are clinically obese")
