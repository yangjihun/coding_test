a,b,c = int(input()),int(input()),int(input())

if a+b+c!=180:
  print("Error")
elif a==b==c:
  print("Equilateral")
elif a!=b and a!=c and b!=c:
  print("Scalene")
else:
  print("Isosceles")