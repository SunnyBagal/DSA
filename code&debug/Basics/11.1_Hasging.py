s = 'azyxyyzaaaa'
q = ['d','a','y','x'] 

# constrainsts: 'a' <= s[i] <= 'z'
hash_map = {}
newArr = s

for i in range(0, len(newArr)):
  hash_map[newArr[i]] = hash_map.get(newArr[i], 0) + 1

for j in q:
  print(hash_map.get(j, 0), end=" ")

print()

s = 'azyxyyzaaaa'
q = ['d','a','y','x']

freq = [0] * 26

# build frequency
for ch in s:
    index = ord(ch) - ord('a')
    freq[index] += 1

# answer queries
for ch in q:
    index = ord(ch) - ord('a')
    print(freq[index], end=" ")