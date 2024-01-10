N,K = map(int,input().split())
data = list(map(int,input().split()))
result = -100
m = 0

for i in range(0,N):
  m += data[i]
  if i>=K:
    m -= data[i-K]
  if result < m and (i+1)>=K:
    result = m
print(result)