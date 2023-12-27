from turtle import Turtle,Screen
import random


screen=Screen()
screen.setup(500,400)
y_positions=[-70,-40,-10,20,50,80]
colours=['red','blue','yellow','green','violet','purple']
all_turtles=[]
for turtle_index in range(0,6):
    new_turtle = Turtle('turtle')
    new_turtle.color(colours[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)



user_bet=screen.textinput('MAKE YOUR BET','WHICH TURTLE WILL WIN THE RACE???')
user_money=screen.numinput("PLACE YOUR MONEY",'PLEASE ENTER THE AMOUNT')


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
    for turtle in all_turtles:
        if turtle.xcor()>230:
           win_colour=turtle.pencolor()
           if win_colour==user_bet:
                print('congrats! you won the race')

           else:
                print('you lost the race')
                print(f'the winner is {win_colour} turtle')
           is_race_on = False

screen.exitonclick()
