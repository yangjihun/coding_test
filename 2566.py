li = []
key = 0
x = 0
y = 0
for i in range(9):
  li.append(list(map(int,input().split())))

for i in range(9):
  for j in range(9):
    if li[i][j]>key:
      key = li[i][j]
      x = i
      y = j

print(key)
print(f"{x+1} {y+1}")
