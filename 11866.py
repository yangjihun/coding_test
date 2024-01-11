N,K = map(int,input().split())
li = list(range(1,N+1))  # 0~N 까지의 수를 저장
ans = []
idx = 0  # 삭제할 index값
while li:  # list가 비워질 때까지 반복
  idx = (idx+K-1)%len(li)  # li 범위를 벗어나지 않게 설정
  ans.append(li[idx])  # answer list에 값 저장
  li.pop(idx%len(li))  # 해당 값 삭제

print('<'+str(ans)[1:-1]+'>')