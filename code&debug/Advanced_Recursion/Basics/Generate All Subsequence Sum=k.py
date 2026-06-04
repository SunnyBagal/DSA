# nums = [5,9,3,4,1]
# target = 9

#! Brute Force 
# res2 = []
# def solve(index, subset):
#   if index >= len(nums):
#     if sum(subset) == target:
#       res2.append(subset.copy())
#     return 
#   subset.append(nums[index])
#   solve(index+1, subset)
#   subset.pop()
#   solve(index+1, subset)

# solve(0, [])
# print(res2)

#~ Time Complexity: O(2 ^ n)
#~ Space Complexity: O(n) ~ size of list

#!——————————————————————————————————————————————————————————————————

#^ Optimal Solution:

nums = [5,9,3,4,1]
target = 12
res = []

def solve(index,total,subset):
  if total == target:
    res.append(subset.copy())
    return   
  elif total > target:
    return
  if index >= len(nums):
    return

  subset.append(nums[index])
  sum = total + nums[index]
  solve(index + 1, sum, subset)
  e = subset.pop()
  sum = sum - e
  solve(index + 1, sum, subset)
   
solve(0, 0, [])
print(res)

#~ Time Complexity: O(2 ^ n) ~ worst case ! in best case its less 
#~ Space Complexity: O(n) ~ size of list