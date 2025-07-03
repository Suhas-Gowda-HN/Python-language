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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("Take correct guess or you wont find the Treasure")
direction = str(input("There is 2 paths in front of you , which direction do you choose? Left or Right : ")).lower()
if direction == "left":
    path = str(input("There is a lake in front of you and the boat arrives in few minutes , what will you choose? Swim or Wait : ")).lower()
    if path == "wait":
       color = str(input("Finally you have reached the final place\nThere are three boxes in front of you\n1. Red\n2. Blue\n3. Yellow\n Only one box contains the 'Treasure'\n what is your choice? red , blue , yellow : ")).lower()
       if color == "yellow":
           print("congrats! you have found the Treasure")
       else:
           print("game over")
    else:
        print("game over")
else:
    print("you fell into the pit hole........\n'game over'")



