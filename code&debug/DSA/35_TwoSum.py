nums = [5,9,1,2,4,15,6,3]

target = 13
n = len(nums)

# for i in range(n):
#   for j in range(i+1, n-1):
#     if nums[i] + nums[j] == target:
#       print(i ,j)



hash_map = {}

for i in range(n):
  remaining = target - nums[i]

  if remaining in hash_map:
    print(hash_map[remaining], i)

  hash_map[nums[i]] = i 
  