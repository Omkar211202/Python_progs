#AUM SRI SAI RAM
print('       The duty assigner    ')
print('    DUTY IS GOD,DO YOUR DUTY      ')
print('                   ')
import random
work = ['suprabhatam', 'miscellaneous', 'foyer', 'night_prayer']  #total duties
t_experts = ['a', 'b', 'c', 'd', 'z', 'y', 'x']  #total experts
t_nibbas = ['e', 'f', 'g', 'h']  #remaining fellows
number = []
total_req = 0
heads = []
check = True
#ensures sufficiency of your need of people to work
while check == True:
  for i in range(0, len(work)):
    user = int(input(f'Enter the no of studs for {work[i]}: '))
    number.append(user)
  for i in number:
    total_req += i
  if total_req > len(t_experts) + len(t_nibbas):
    print('you need more boys than you have')
  else:
    check = False
#choosing the heads
counter=0
while counter<=len(work):
  b=random.choice(t_experts)
  if b in heads:
    counter=counter-1
  else:
    heads.append(b)
#who forms the remaining
for i in range(0, len(t_experts)):
  if t_experts[i] not in heads:
    t_nibbas.append(t_experts[i])
print('                          ')
print("the final list goes like:")
already = []
#forming the whole team:
for i in range(0, len(work)):
  fi = []
  a = heads[i]
  fi.append(a)

  for j in range(0, number[i] - 1):
    vi = random.choice(t_nibbas)
    while vi in already:
      vi = random.choice(t_nibbas)
    fi.append(vi)
  print(f'{work[i]}: {str(fi)}')
