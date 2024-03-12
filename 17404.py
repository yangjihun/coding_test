# 1번 집의 색은 2번, N번 집의 색과 같지 않아야 한다.
# N번 집의 색은 N-1번, 1번 집의 색과 같지 않아야 한다.
# i(2 ≤ i ≤ N-1)번 집의 색은 i-1, i+1번 집의 색과 같지 않아야 한다.

N = int(input())
result = [[0,0],[0,0],[0,0]]
first = list(map(int,input().split()))

for i in range(2,N+1):
  rgb = list(map(int,input().split()))
  if i==2:
    result = [[rgb[0]+first[1],rgb[0]+first[2]],[rgb[1]+first[0],rgb[1]+first[2]],[rgb[2]+first[0],rgb[2]+first[1]]]
  if i==N:
    print(min([min([rgb[0]+min(result[1]),rgb[0]+min(first[2])]),min([rgb[1]+min(first[0]),rgb[1]+min(first[2])]),min([rgb[2]+min(first[0]),rgb[2]+min(first[1])])]))
  else:
    result = [[[rgb[0]+min(result[1],result[2])]*2],[[rgb[1]+min(result[0],result[2])]*2],[[rgb[2]+min(result[0],result[1])]*2]]