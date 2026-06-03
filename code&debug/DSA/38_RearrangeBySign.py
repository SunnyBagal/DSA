nums = [5,10,-3,-1,-10,6]
n = len(nums)
res = [0] * n
pos , neg = 0 , 1

for i in range(n):
  if nums[i] >= 0:
    res[pos] = nums[i]
    pos += 2
  if nums[i] < 0:
    res[neg] = nums[i]
    neg += 2

print(res)

#~ TC : O(N)
#~ SC : O(1)/ O(N)

