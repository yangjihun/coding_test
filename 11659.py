#N,M = map(int,input().split())
#li = list(map(int,input().split()))
#A = [0]
#temp = 0
#for i in li:
#  temp+=i
#  A.append(temp)

#for i in range(M):
#  s,e = map(int,input().split())
#  print(A[e]-A[s-1])
# sys를 안써서 시간초과가 떴음
# 밑에 코드는 같은 코드인데 sys를 이용한 코드 (time error가 안났음)
import sys
input = sys.stdin.readline
 
m, n = map(int, input().split())
arr = list(map(int, input().split()))
prefix_sum = [0]
temp = 0    
for i in arr:
    temp += i
    prefix_sum.append(temp)
 
for i in range(n):
    a, b = map(int, input().split())
    print(prefix_sum[b] - prefix_sum[a-1])