N = int(input())
if N%2==1:
  print(0)
else:
  result = 3
  for _ in range(1,N//2):
    result = result*3+2
  print(result)