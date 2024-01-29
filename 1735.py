a1,b1 = map(int,input().split())
a2,b2 = map(int,input().split())

i,j = b1,b2
while j>0:
  i,j = j,i%j
b = b1*b2//i
a = a1*(b//b1) + a2*(b//b2)
print(a,b)