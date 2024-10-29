import sys
input = sys.stdin.readline

N,M = map(int,input().split())
table = []

for _ in range(N):
  table.append(list(map(int,input().split())))

A = table

for i in range(N):
  for j in range(N):
    A[i][j] +=  table[i-1][j] + table[i][j-1] - table[i][j]
print(A)