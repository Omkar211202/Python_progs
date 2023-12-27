from replit import clear
var="yes"
dictionary={}
list=[]
highest_bid=0
def find_highest_bid(dictionary):
  for i in dictionary:
    if dictionary[i]>highest_bid:
      highest_bid=dictionary
  print(highest_bid)
while var == "yes":
  name=input('please tell us your name')
  value=int(input("please enter your auction value"))
  dictionary[name]=value
  var=input('tell us if there any more bids, yes or no')
  if var == 'yes':
    clear()
find_highest_bid()
