# 263A. Bit++
n = int(input())
x = 0

for i in range(n) :
    bit = str(input())
    if '++' in bit :
        x += 1
    elif '--' in bit :
        x -= 1
        
print(x)