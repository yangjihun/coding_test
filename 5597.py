num_list = [i for i in range(1,31)]

for _ in range(28):
  num_list[int(input())-1] = 0

for i in num_list:
  if i!=0:
    print(i)