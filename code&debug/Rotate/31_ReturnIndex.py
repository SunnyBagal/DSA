nums = [5,3,2,1,5,6,67,0]
key = 1
def index(nums,k):
  for i in range(len(nums)):
    if nums[i] == k:
      return i
  return -1

print(index(nums,key))

  

