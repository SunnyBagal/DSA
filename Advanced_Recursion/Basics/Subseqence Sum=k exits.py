nums = [5,9,4]
target = 9
res = []
def backtrack(index,total):
  if total == target:
     return True
  elif total > target:
     return False
  if index >= len(nums):
     return False
  Sum = total + nums[index]
  pick = backtrack(index + 1, Sum)
  if pick == True: 
    return True
  Sum = total
  not_pick = backtrack(index + 1, Sum)
  return not_pick

print(backtrack(0,0))

#~ Time Complexity: O(2 ^ n)
#~ Space Complexity: O(n) ~ size of list