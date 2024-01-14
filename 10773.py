K = int(input())
li = []
for _ in range(K):
  n = int(input())
  li.append(n) if n!=0 else li.pop()
print(sum(li))