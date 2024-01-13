import sys
n = int(sys.stdin.readline())
li = []

for i in range(n):
  an = sys.stdin.readline().split()
  if an[0]=="1":
    li.append(an[1])
  elif an[0]=="2":
    print(li.pop()) if len(li)!=0 else print(-1)
  elif an[0]=="3":
    print(len(li))
  elif an[0]=="4":
    print(0) if len(li)!=0 else print(1)
  elif an[0]=="5":
    print(li[-1]) if len(li)!=0 else print(-1)

# sys 추가하니까 타임에러 안뜸