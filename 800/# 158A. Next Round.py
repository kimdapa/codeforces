# 158A. Next Round
n, k = map(int, input().split())
participants = list(map(int, input().split()))
winner = 0
participants.sort(reverse = True)

for participant in participants :
    if participant > 0 and participant >= participants[k-1] :
            winner += 1
    else :
        pass
    
print(winner)