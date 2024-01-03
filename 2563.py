N = int(input())
map_array = [[0]*100 for _ in range(100)]
answer = 0

for _ in range(N):
  x,y = map(int,input().split())
  for i in range(x,x+10):
    for j in range(y,y+10):
      map_array[i][j] = 1
for i in map_array:
  for j in i:
    if j==1:
      answer+=1
print(answer)