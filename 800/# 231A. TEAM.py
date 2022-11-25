# 231A. TEAM
n = int(input())
count = 0

for i in range(n) :
    p,v,t = map(int, input().split())
    if (p+v+t) == 3 or (p+v+t) == 2 :
        count += 1
    else : 
        pass

print(count)