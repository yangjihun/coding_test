jinsu_2 = input()
jinsu_8 = ''

# 2진수 3개씩 끊기
jinsu_2 = '0'*(3-len(jinsu_2)%3) + jinsu_2


for i in range(0,len(jinsu_2),3):
  key = 2
  add = 0
  for k in jinsu_2[i:i+3]:
    add += int(k)*(2**key)
    key-=1
  jinsu_8+=str(add)
if jinsu_8[0]=='0' and len(jinsu_8)!=1:
  jinsu_8 = jinsu_8[1:]
print(jinsu_8)