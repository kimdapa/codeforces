# 263A. Beautiful Matrix
count = 0 

for i in range(5) :
    M = list(map(int, input().split()))
    if i == 0 or i == 4 and 1 in M : # 1, 5 번째 행에 1이 있을 때 
        if M[0] == 1 or M[4] == 1 :
            count += 4
        elif M[1] == 1 or M[3] == 1 :
            count += 3
        elif M[2] == 1 :
            count += 2
    elif i == 1 or i == 3 and 1 in M : #2, 4 번째 행에 1이 있을 때 
        if M[0] == 1 or M[4] == 1 :
            count += 3
        elif M[1] == 1 or M[3] == 1 :
            count += 2
        elif M[2] == 1 :
            count += 1
    elif i == 2 and 1 in M : # 3번째 행에 1이 있을 때 
        if M[0] == 1 or M[4] == 1 :
            count += 2
        elif M[1] == 1 or M[3] == 1 :
            count += 1

print(count)