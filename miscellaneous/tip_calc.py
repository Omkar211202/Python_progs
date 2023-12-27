#TIP CALCULATOR 
#This programme takes total bill in hotel,levies a tip percent inputed and divides the
entire cost among a certain number of people.
cost=int(input("please enter the total cost levied onto you?"))
tip=int(input("please tell us the percentage of tip you would like to pay...."))
people=int(input("please tell the number of people on whom you would like the bill to be shared..."))

#total bill
total=cost+tip/100*cost
each=total/people
print("each pay the following amount" + each + "to us")
# to make the program more precise repalce cost and tip as float datatypes.




