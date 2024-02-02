D,B = map(int,input().split())
li = {}
for _ in range(D):
  li[input()] = 0

for _ in range(B):
  name = input()
  if li[name]:
    print(name)