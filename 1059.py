S = int(input())
li = list(map(int,input().split()))
n = int(input())
answer = 0

for i in range(0,S-1):
  if li[i]<n and li[i+1]>n:
    le = li[i+1]-li[i]-1
    for k in range(0,n-li[i]):
      answer+=(le-k-1)
print(answer)