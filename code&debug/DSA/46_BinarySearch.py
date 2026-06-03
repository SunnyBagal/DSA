
#^ BINARY SEARCH 
#! NOTE: the list shuold be sorted 


nums = [2,4,6,7,9,11,18,19]
nums.sort()

target = 6
low = 0
high = len(nums) - 1

while low <= high:
    mid = (low + high) // 2
    
    if target < nums[mid]:
        high = mid - 1
        
    elif target > nums[mid]:
        low = mid + 1
        
    else:
        print("Found at index:", mid)
        break
    

# def binarySearch(nums, low, high):
#       if low > high:
#           return - 1
#       mid = (low+high)// 2
#       if nums[mid] == target:
#           return mid 
#       elif nums[mid] < target:
#           return binarySearch(nums, mid+1, high)
#       else :
#           return binarySearch(nums, low, mid-1)
      
# print(binarySearch(nums, 0, len(nums)))

#~ TC: O(log2 (N)) N-> is the number of elements in list 
#~ SC: O(1)