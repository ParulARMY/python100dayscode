#In this program we will use f-string.

age=int(input("What is your current age"))
rem_age= 90-age
days =int(rem_age*365)
weeks= int(rem_age*52)
months = int(rem_age*12)
print(f"you have{days} Days ,{weeks} Weeks , {months} Months left")