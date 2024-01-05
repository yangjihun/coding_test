word = input().upper()
key = 0
result = ''

letter = dict(zip(set(word),[0]*len(set(word))))
for i in word:
  letter[i]+=1
value = letter.values()
for i in letter.keys():
  if letter[i]==max(value):
    key+=1
    result = i
    if key==2:
      result = '?'
      break
print(result)