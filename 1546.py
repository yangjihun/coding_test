N = int(input())
score = list(map(int,input().split()))
m = max(score)
sum_score = 0
for i in range(N):
  sum_score += score[i]*100/m
print(sum_score/N)