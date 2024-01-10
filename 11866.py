N,K = map(int,input().split())
li = list(range(1,N+1))
ans = []
idx = 0
while li:
  idx = (idx+K-1)%len(li)
  ans.append(li[idx])
  li.pop(idx%len(li))

print('<'+str(ans)[1:-1]+'>')