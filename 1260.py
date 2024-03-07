import sys
from collections import deque

input = sys.stdin.readline
N,M,V = map(int,input().split())
li = [[] for _ in range(N+1)]
que = deque(deque() for _ in range(N+1))
q = deque([V])
li_visited = [False for _ in range(N+1)]
que_visited = [False for _ in range(N+1)]
print(li_visited)

for i in range(M):
  a,b = map(int,input().split())
  li[a].append(b)
  que[a].append(b)
  li[b].append(a)
  que[b].append(a)

def DFS(v):
  li_visited[v] = True
  print(v,end=' ')
  for i in li[v]:
    if not li_visited[i]:
      DFS(i)

def BFS():
  if not que_visited[q[0]]:
    que_visited[q[0]] = True
    for i in li[q[0]]:
      if not que_visited[i]:
        q.append(i)
    print(q.popleft(),end=' ')
    if q:
      BFS()

DFS(V)
print()
BFS()

