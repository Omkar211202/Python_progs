import requests
import tkinter
connection=requests.get(url="https://opentdb.com/api.php?amount=10&category=9&difficulty=medium&type=boolean")
count=0
score=0
for i in range(0,10):
  data=connection.json()['results'][count]["question"]
  print(data)
  answer=connection.json()['results'][count]['correct_answer']
  resp=input('please enter True or False:')

  if resp==answer:
    print("thats the correct answer")
    score+=1
  else:
    print('thats the wrong answer')
  count+=1
