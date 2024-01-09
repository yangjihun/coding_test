T = int(input())
for _ in range(T):
  key = 0
  a,b = map(int,input().split())
  for i in range(1,a//2+1):
    if (b*i)%a==0:
      print(b*i)
      key = 1
      break
  if key==0:
    print(a*b)