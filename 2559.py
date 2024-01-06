N,K = map(int,input().split())
data = list(map(int,input().split()))
result = -100
A = [0]*(N+1)

for i in range(1,N+1):
  A[i] = A[i-1]+data[i-1]

for i in range(0,N-K+1):
  if result<A[i+K]-A[i]:
    result = A[i+K]-A[i]
print(result)