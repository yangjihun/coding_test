# input
N = int(input())
li = [0]
for _ in range(N):
  li.append(int(input()))
li = li[::-1]
result = li[0]

for i in range(1,N,2):
  result += max(li[i],li[i+1])

print(result)