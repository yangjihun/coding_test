N = int(input())
gap = 1000000
i = int(input())
li = [i]
result = 0

for _ in range(N-1):
  j = int(input())
  if j-i<gap:
    gap = j-i
  i = j
  li.append(i)

for x in range(N-1):
  g = (li[x+1]-li[x])//gap-1 if (li[x+1]-li[x])//gap==gap else (li[x+1]-li[x])//gap
  result += g
print(result)