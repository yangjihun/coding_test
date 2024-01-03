s,e = map(int,input().split())
li = list()
key = 1
while len(li)<e:
  li+=[key]*key
  key+=1

A = [0]*(len(li)+1)
for i in range(1,len(li)+1):
  A[i] = A[i-1]+li[i-1]

print(A[e]-A[s-1])