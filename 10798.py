li = list()
m = 0
answer = ''
for _ in range(5):
  li.append(input())
  if len(li[-1])>m:
    m = len(li[-1])

for i in range(m):
  for x in range(5):
    if len(li[x])>i:
      answer += li[x][i]
print(answer)