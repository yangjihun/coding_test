N = int(input())
A = list(map(int,input().split()))[::-1]
li = []

for i in A:
  if li and li[-1]<i:
    li.pop()
  else:
    li.append()
print(li)