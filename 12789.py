N = int(input())
li = list(map(int,input().split()))
stack = []
key = 1

while li:
  if li[0]==key:
    li.pop(0)
    key+=1
  else:
    stack.append(li.pop(0))
  
  while stack:
    if stack[-1]==key:
      stack.pop()
      key+=1
    else:
      break
print('Nice' if not stack else 'Sad')