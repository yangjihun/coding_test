N,K = map(int,input().split())
A = [[1 for _ in range(N+1)] for i in range(K)]
for i in range(1,K):
  for j in range(1,N+1):
    A[i][j] = (A[i-1][j] + A[i][j-1])%1000000000
print(A[K-1][N])