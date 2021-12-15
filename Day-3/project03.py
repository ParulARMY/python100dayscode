print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')

print("Welcome to the Treasure island")
print("Your mission is to find the treasure.")
choice1 = input('You\' re at a crossroad, where do you want to go? type "left" or "right". ').lower()

if choice1 == "left":
    choice2 = input(
        'You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" wait for the boat. Or type "swim"  swim across \n').lower()
    if choice2 == "wait":
        choice3 = input(
            "You have arrive the island unharmed. There is a house with three door. One is red, One is yellow and  One is blue. Which color do you chosse?\n").lower()
        if choice3 == "red":
            print("It's a room of full of fire. Game Over.\n")
        elif choice3 == "yellow":
            print("You find the treasure! You win the game\n")
        elif choice3 == "blue":
            print("You enter room of breast. Game Over.\n")
        else:
            print("You chosse the that door that doesn't exist.  Game over.\n")
    else:
        print("You got Attacked by an angry trout. Game Over.\n")
else:
    print("You fell into a hole. Game Over.")
