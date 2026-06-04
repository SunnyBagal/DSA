nums = [5,1,9,3,4]
k = 9

def countSubs(index,total,):
  if total == k:
    return 1
  elif total > k:
    return 0
  if index >= len(nums):
    return 0
  
  sum = total + nums[index]
  pick = countSubs(index+1, sum)
  sum = total
  not_pick = countSubs(index+1, sum)
  return pick + not_pick

print(countSubs(0,0))


#~ Time Complexity: O(2 ^ n)
#~ Space Complexity: O(n) ~ size of stack