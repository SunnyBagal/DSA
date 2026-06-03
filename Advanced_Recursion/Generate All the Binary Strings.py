# nums = [3,4,5,1,2]
# n = len(nums)
# left = 0
# right = n - 1
# mini = nums[0]

# while left < right:
#   mid = (left + right)// 2

#   if nums[mid] < nums[right]:
#     mini = min(mini, nums[mid])
#     right = mid - 1

#   else: 
#     mini = min(mini, nums[left])
#     left = mid + 1

# print(mini)

# #! Valid perfect square:
num = 16
left = 1
right = num

while left <= right:
  mid = (right + left) //2
  mid_sqred = mid * mid

  if num == mid_sqred:
    print(True)
    break
  elif mid_sqred < num:
    left = mid + 1
  else:
    right = mid - 1


