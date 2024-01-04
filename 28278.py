import sys
input = sys.stdin.readline
li = list()
n = int(input())

for _ in range(n):
  an = input()
  if an[0]=="1":
    li.append(int(an[1:]))
  elif an=="2":
    if len(li)==0:
      print(-1)
    else:
      print(li[-1])
      li.pop()
  elif an=="3":
    print(len(li))
  elif an=="4":
    if len(li)==0:
      print(1)
    else:
      print(0)
  elif an=="5":
    if len(li)==0:
      print(-1)
    else:
      print(li[-1])