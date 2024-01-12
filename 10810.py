N,M = map(int,input().split())
basket = [0]*N

for _ in range(M):
  s,e,k = map(int,input().split())
  for i in range(s-1,e):
    basket[i] = k
for i in basket:
  print(i,end=' ')