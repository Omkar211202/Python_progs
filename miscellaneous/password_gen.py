import random
number = random.randint(1,100)
level=input("choose your level:'easy' or 'difficult'\n")
if level == 'easy':
    attempts=10
elif level == 'difficult':
    attempts=5
determinant='yes'
while attempts > 0:
    user=int(input('guess a number between 1 to 100\n'))
    if user == number:
        print('congrats! you won')
        attempts-=10
    elif user > number:
        print('your choice is high')
        attempts-=1
    elif user < number:
        print('your choice is too low')
        attempts-=1
    if attempts > 0:
       print(f'you have only {attempts} attempts left...')

#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
#simple and easy method follows no shuffling
password=""
for i in range(0,nr_letters):
  letter=random.randint(0,51)
  password+=letters[letter]

for i in range(0,nr_numbers):
  letter=random.randint(0,9)
  password+=numbers[letter]

for i in range(0,nr_symbols):
  letter=random.randint(0,8)
  password+=symbols[letter]
print(password)
#reshuffling the list
list=[]
for i in password:
  list.append(i)
random.shuffle(list)
#convering list to string
final_password=''
for i in list:
  final_password+=i
print(final_password)
  
