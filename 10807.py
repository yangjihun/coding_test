N = int(input())
li = list(map(int,input().split()))
k = int(input())
result = 0
for i in li:
    if i==k:
        result+=1
print(result)