N = int(input())
result = 0
for i in range(1,N):
  if i>N:
    break
  else:
    result+=1
    N-=i
print(result)