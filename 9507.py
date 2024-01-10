t = int(input())
koong = [1,1,2,4]

while len(koong)!=68:
  koong.append(koong[-1]+koong[-2]+koong[-3]+koong[-4])
for _ in range(t):
  print(koong[int(input())])