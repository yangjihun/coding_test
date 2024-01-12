num_list = []
for _ in range(10):
  a = int(input())
  if (a%42 not in num_list)==1:
    num_list += [a%42]
print(len(num_list))