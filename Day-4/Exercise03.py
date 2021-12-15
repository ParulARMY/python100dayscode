#BAnker Roulette
import random
names_String = input("Give me everybody's name seperated by a comma")
names= names_String.split(",")
print(names)
num_items = len(names)
choice = random.randint(0,num_items-1)
person = names[choice]
print(person +"is going to buy the meal toady")