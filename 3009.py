def compare(li):
  if li[0]==li[1]:
    return li[2]
  elif li[0]==li[2]:
    return li[1]
  else:
    return li[0]

x = list()
y = list()

for _ in range(3):
  a,b = map(int,input().split())
  x.append(a)
  y.append(b)

print(compare(x), compare(y))