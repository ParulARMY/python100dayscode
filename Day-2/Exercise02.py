#we used two print statement because bmi is in int to overcome we will use in f_string.
height = float(input("Enter your height in meters\n"))
weight = float(input("Enter your weight in kgs\n"))
bmi = weight/(height*height)
print("your BMI is: ")
print(int(bmi))