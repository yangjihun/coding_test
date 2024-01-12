N,M = map(int,input().split())
basket = [i+1 for i in range(N)]

for _ in range(M):
  a,b = map(int,input().split())
  li = basket[a-1:b]
  for i in range(len(li)):
    basket[a-1+i] = li[-(i+1)]

for i in basket:
  print(i, end=' ')