nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

currentSum = 0
maxSum = nums[0]

for i in nums : 
  currentSum += i
  if currentSum > maxSum:
    maxSum = currentSum
  if currentSum < 0:
    currentSum = 0
print(maxSum)

maxi = float('-inf')
n = len(nums)
for i in range(n):
  total = 0
  for j in range(i, n):
    total = total + nums[j]
    maxi = max(maxi, total)

print(maxi) 