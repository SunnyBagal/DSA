nums = [1,7,3,6,5,6]
nums = [2,1,-1]

left = 0
n = len(nums)
count = 0
for i in range(n):
  if left == sum(nums) - left - nums[i]:
    print(i)
  left += nums[i]


