for i in range(0, n):
  hash_map[nArr[i]] = hash_map.get(nArr[i], 0) + 1

for num in mArr:
    print(hash_map.get(num, 0), end=" ")