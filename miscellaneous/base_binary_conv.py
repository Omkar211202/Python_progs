number=int(input("please enter the number:"))
base=int(input("please enter the base:"))
check=base-1
dic_rfr={10:"A",11:"B",12:"C",13:"D",14:"E",15:"F"}
list=[]
while number>check:
  det=int(number%base)
  number=int(number/base)
  list.append(det)
for i in list:
  if i > 9:
    list[list.index(i)]=dic_rfr[i]

list.append(number%base)
list.reverse()
a=''.join(str(e)for e in list)
print('your are answer=',a)


