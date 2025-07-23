import random
p1 = 0
p2 = 0
p3 = 0

for i in range(10001):
    x = random.randint(1,6)
    y = random.randint(1,6)
    s = x+y
    if s == 2:
        p1+=1
    elif s == 7:
        p2+=1
    elif s > 10:
        p3+=1

p1 = p1/10000
p2 = p2/10000
p3 = p3/10000

print(p1,p2,p3)

