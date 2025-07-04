import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
print("Welcome to Rock , Paper , Scissors Game!")
num = int(input("Choose\nNumber 1 for rock\nNumber 2 for paper\nNumber 3 for scissors:\n"))
if num == 1:
    print("you chose")
    print(rock)
elif num == 2:
    print("you chose")
    print(paper)
elif num == 3:
    print("you chose")
    print(scissors)
else:
    print("choose valid option")

print("\ncomputer chose")
com = [rock, paper, scissors]
computer = random.randint(0,2)
print(com[computer])

if num == 1 and computer == 0:
    print("Its a Draw")
elif num == 1 and computer == 1:
    print("you lose")
elif num == 1 and computer == 2:
    print("you win")
elif num == 2 and computer == 1:
    print("Its a Draw")
elif num == 2 and computer == 2:
    print("you lose")
elif num == 2 and computer == 0:
    print("you win")
elif num == 3 and computer == 2:
    print("Its a Draw")
elif num == 3 and computer == 0:
    print("you lose")
elif num == 3 and computer == 1:
    print("you win")