stones = 'aA'
jewels = "aAAbbbb"

n = len(jewels)
m = len(stones)
hash_map = {}
sum = 0

for i in range(n):
    hash_map[jewels[i]] = hash_map.get(jewels[i], 0) + 1

for j in stones:
    new = hash_map.get(j, 0)
    sum = sum + new
    
print(sum)  