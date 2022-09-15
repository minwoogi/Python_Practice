N = int(input())
score = list(map(int,input().split()))
maxScore = max(score)
answer = 0

for i in score:
    answer += i/maxScore*100
print(answer/N)