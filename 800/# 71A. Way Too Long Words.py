# 71A. Way Too Long Words
n = int(input())

for i in range(n) :
    k = str(input())
    if len(k) > 10 :
        sentence = list(k)
        len_sentence = len(sentence) - 2
        print(sentence[0] + str(len_sentence) + sentence[-1])
    else :
        print(k)