import sys
from collections import deque

input = sys.stdin.readline
N,M,V = map(int,input().split())
li = [[] for _ in range(N+1)]
que = deque(deque() for _ in range(N+1))
li_visited = [False for _ in range(N+1)]
que_visited = [False for _ in range(N+1)]

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

def BFS(v):
  q = deque([v])
  while q:
    v = q.popleft()
    que_visited[v] = True
    print(v,end=' ')
    for i in li[v]:
      if not que_visited[i]:
        q.append(i)

DFS(V)
print()
BFS(V)

