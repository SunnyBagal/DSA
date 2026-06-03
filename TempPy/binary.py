nums = [1,2,3,4,5,6,7,8]
target = 7

n = len(nums)
start = 0
end = n - 1

while start < end:
  mid = (start + end)//2

  if nums[mid] == target:
      print(mid) 
      break
  
  elif nums[mid] < target :
      start = mid + 1
  
  elif nums[mid] > target:
      end = mid - 1