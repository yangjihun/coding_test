# 괄호 문자열
for _ in range(int(input())):
  s = input()
  li = []
  for k in s:
    if k==')' and len(li)>0 and li[-1]=='(':
      li.pop()
    else:
      li.append(k)
  if len(li)!=0:
    print('NO')
  else:
    print("YES")