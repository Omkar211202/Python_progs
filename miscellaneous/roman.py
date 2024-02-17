l = []
lr = []
final = []
roman = ''

inp = 10
lr.append(inp)

inp1 = (inp//1000)
inp2 = inp%1000
l.append(inp1)
lr.append(inp2)
for i in range(0,l[0]):
    final.append('M')
    
inp = inp2
inp1 = inp//100
inp2 = inp%100
l.append(inp1)
lr.append(inp2)
if l[1] < 4 and l[1] >= 1:
    for i in range(0, l[1]):
        final.append('C')
if l[1] == 4:
    final.append('CD')
if l[1] == 5:
    final.append('D')
if l[1] > 5 and l[1] < 9:
    final.append('D')
    for i in range(0, l[1]-5):
        final.append('C')
if l[1] == 9:
    final.append('CM')

inp = inp2
inp1 = inp//10
inp2 = inp%10
l.append(inp1)
lr.append(inp2)
if l[2] < 4 and l[2] >= 1:
    for i in range(0, l[2]):
        final.append('X')
if l[2] == 4:
    final.append('XL')
if l[2] == 5:
    final.append('L')
if l[2] > 5 and l[2] < 9:
    final.append('L')
    for i in range(0, l[2]-5):
        final.append('X')
if l[2] == 9:
    final.append('XC')


inp = inp2
inp1 = inp%10
l.append(inp1)
if l[3] < 4 and l[3] >= 1:
    for i in range(0, l[3]):
        final.append('I')
if l[3] == 4:
    final.append('I')
if l[3] == 5:
    final.append('V')
if l[3] > 5 and l[3] < 9:
    final.append('V')
    for i in range(0, l[3]-5):
        final.append('I')
if l[3] == 9:
    final.append('IX')

for i in final:
    roman += i

print(roman)
