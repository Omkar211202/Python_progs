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

