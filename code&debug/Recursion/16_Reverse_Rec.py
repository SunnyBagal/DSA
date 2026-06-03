nums = [1,2,3,4,5,6,7,8,9]
# print(nums[::-1])

def Reverse(arr, left, right):
  if left >= right:
    return arr
  
  arr[left], arr[right] = arr[right], arr[left]
  return Reverse(arr, left+1, right-1)

print(Reverse(nums, 1,3))

#~ TC : O(N/2)
#~ SC: O(N/2) -> Stack Space