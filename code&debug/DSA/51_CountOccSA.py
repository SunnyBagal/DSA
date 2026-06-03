nums = [1,2,3,3,3,3,3,5,6,8,9,9,10]
n = len(nums)
target = 3
first = -1
last = -1

for i in range(n):
  if nums[i] == target:
    if first == -1:
      first = i
    last = i

print((last - first) + 1)


def lowerBound(nums,target):
  n = len(nums)
  lb = -1
  low = 0
  high = n - 1
  while low <= high:
    mid = (low+high)//2
    if nums[mid] >= target:
      lb = mid
      high = mid - 1
    else:
      low = mid + 1
  return lb

def upperBound(nums, target):
  n = len(nums)
  ub = n
  low = 0
  high = n - 1
  while low <= high:
    mid = (low+high)//2
    if nums[mid] > target:
      ub = mid
      high = mid - 1
    else:
      low = mid + 1
  return ub  

lower_bound = lowerBound(nums, 3)
upper_bound = upperBound(nums, 3)
print((upper_bound - lower_bound))
