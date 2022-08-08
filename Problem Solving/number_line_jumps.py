x1 = 2
v1 = 1
x2 = 1
v2 = 2

boolMe = False

while(x1 != x2):
    x1 += v1
    x2 += v2
    if x1 == x2:
        boolMe = True
        break
print(boolMe)