import random
print('THIS GAME ASKS YOU TO GUESS A WORD ! ALL THE VERY BEST')
#the word list
word_list = ["aardvark", "baboon", "camel","sashank"]
right=0
wrong=6
#we must know the last index in the list so:
number=len(word_list)-1
chosen_word=word_list[random.randint(0,number)]
#the above line randomly chooses a word from the list and the below puts the correct number of strips knowing the how long the word is
blank=len(chosen_word)
print(f"the following word has {blank} letters... \nctry your luck...")
strip=''
for i in range(0,blank):
  strip+='_'
print(strip)
#converting the strip into a list for operations
list=[]
for i in range(0,blank):
  list.append('_')
#converting the chosen word into a list.
a=[]
for i in chosen_word:
  a.append(i)
#the following are the pics of hangman
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
#while loop comes here, it keeps the game going till one of the condition is Broken
while '_' in list and wrong > 0:
#the user is asked for input,
  guess=input('Guess a letter \n')
  guess=guess.lower()
  if guess in a :#a is the list of letters in the chosen word.
     print('you guessed the correct letter..')
  else:
    wrong-=1
    print (f'you guessed a wrong letter! you have {wrong} chances')
  for i in range(0,len(chosen_word)):
    if a[i]== guess:#this checks if guess equals a letter in the chosen word.
       list[i]=guess
  word=''#convert list to string ____
  for i in list:
    word+= i
  print(word)
  print(stages[wrong])
#the while loop is broken and its decided if a person won the game or not.
if '_' not in list:
  print("congrats! you won the game")
else:
  print("bad luck! try again")
