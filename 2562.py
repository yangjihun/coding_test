result = 0
idx = 0
for i in range(1,10):
  num = int(input())
  if num > result:
    result = num
    idx = i
print(result)
print(idx)