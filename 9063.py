def length(li):
  if len(li)==1:
    return 0
  return (max(li)-min(li))

N = int(input())
x = list()
y = list()

for _ in range(N):
  a,b = map(int,input().split())
  x.append(a)
  y.append(b)
print(length(x)*length(y))
