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

#Write your code below this line 👇

games_image=[rock, paper, scissors]

u_choice=int(input("What is your choice: 0.Rock , 1. Paper, 2. Scissors "))
if u_choice <0 or u_choice >2:
    print("Invalid Choice")
else:
    print(u_choice)
    print(f"User choice:\n{games_image[u_choice]}")
    com_choice=random.randint(0,2)
    print(com_choice)
    print(f"Computer Choice:\n {games_image[com_choice]}")

    if u_choice == 0 and com_choice == 2:
        print("You Won")
    elif u_choice == 2 and com_choice == 0:
        print("You Lose")
    elif u_choice > com_choice:
        print("You Won")
    elif u_choice == com_choice:
        print("Draw")
    else: 
        print("You lose")


