nums = [2,2,1,1,1,2,2]
n = len(nums)
hash_map = {}

for i in range(n):
    hash_map[nums[i]] = hash_map.get(nums[i], 0 ) + 1



