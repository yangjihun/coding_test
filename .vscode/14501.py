N = int(input())
li = [[] for _ in range(N)]
for i in range(N):
  li[i] = list(map(int,input().split()))

for i in range(N):
  li[i]