#THIS IS THE ROCK,PAPER AND SCISSORS GAME.
#CHOICE=MY CHOICE AND COMPUTER=COMPUTERS RANDOM CHOICE.
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
import random
choice=int(input('choose 0 for rock,1 for paper and 2 for scissors.'))
computer=random.randint(0,2)
print("you chose:)
if choice == 0:
  print(rock)
elif choice == 1:
  print(paper)
else:
  print(scissors)
if computer == 0:
  print(rock)
elif computer == 1:
  print(paper)
else:
  print(scissors)
print("the computer by sheer luck chooses")
if choice == computer:
  print("draw")
if choice == 0 and computer == 1:
  print("you lost")
elif choice == 0 and computer == 2:
  print("you won")
elif choice == 1 and computer == 0:
  print('you won')
elif choice == 1 and computer == 2:
  print("you lost")
elif choice == 2 and computer == 0:
  print('you lost')
elif choice == 2 and computer == 1:
  print ("you won")


