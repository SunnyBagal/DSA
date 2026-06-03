nums = [1,2,13,4,19,5,6,7,8]
n = len(nums)
slar = float('-inf')
lar = nums[0]

for i in range(1,n):
  if nums[i] > lar:
    slar = lar
    lar = nums[i]

  if nums[i] > slar and nums[i] != lar:
    slar = nums[i]

print(slar)

#~ TC: O(N)
#~ SC: O(1)