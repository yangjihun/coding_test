t = int(input())  # t = 질문 개수
koong = [1,1,2,4]  # list  안에 [koong(0), koong(1), koong(2), koong(3)] 저장 

while len(koong)!=68:  # n의 최대 수만큼 koong에 값 추가
  koong.append(koong[-1]+koong[-2]+koong[-3]+koong[-4])

for _ in range(t):  # 질문 수만큼 결과값 출력
  print(koong[int(input())])