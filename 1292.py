s,e = map(int,input().split())
li = list()

for i in range(1,1001):
  li+=[i]*i
  if len(li)>=e:
    break

A = [0]*(len(li)+1)
for i in range(1,len(li)+1):
  A[i] = A[i-1]+li[i-1]

print(A[e]-A[s-1])