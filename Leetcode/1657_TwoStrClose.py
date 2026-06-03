word1 = 'abc'
word2 = 'bca'

n = len(word1)
m = len(word2)

if n != m :
  print(False)

num_map1 = []
num_map2 = []

for i in range(97,123):
  if chr(i) in word1 and chr(i) in word2:
    num_map1.append(word1.count(chr(i)))
    num_map2.append(word2.count(chr(i)))

  elif (chr(i) in word1 and chr(i) not in word2 or chr(i) in word2 and chr(i) not in word1):
    print(False)

num_map1.sort()
num_map2.sort()
if num_map1 == num_map2:
  print(True)



