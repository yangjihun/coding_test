def fib(n):
  if n==1 or n==2:
    return 1
  else:
    return fib(n-1)+fib(n-2)

def fibonacci(n):
  f = [1,1]
  for i in range(3,n):
    f.append(f[-1]+f[-2])
  return len(f)-1

n = int(input())
print(fib(n),fibonacci(n))