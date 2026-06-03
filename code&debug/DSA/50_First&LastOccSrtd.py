
#* Find the first and last occurrence of a target 

nums = [1,2,3,3,3,3,3,5,6,8,9,9,10]
n = len(nums)
# first_occ = -1
# last_occ = -1
# target = 3

# i = 0
# for i in range(n):
#   if nums[i] == target:
#     if first_occ == -1:
#       first_occ = i
#     last_occ = i


# print(first_occ, last_occ)

nums2 = [1]
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
  return ub -1 

lower_bound = lowerBound(nums2, 1)
upper_bound = upperBound(nums2, 1)
print(lower_bound,upper_bound)

#~ TC: O(2log N) ~ O(log N)
#~ SC: O(1)
