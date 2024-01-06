want = int(input())
storage = []
num = [64,32,16,8,4,2,1]

for i in num:
  if want-i>=0:
    want-=i
    storage.append(i)
print(len(storage))