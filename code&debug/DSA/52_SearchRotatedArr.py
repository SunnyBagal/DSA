
#* Search in rotated sorted array 

nums = [17,18,20,1,3,4,5,7,8,10,11,13,14,16]
target = 4

low = 0
high = len(nums) - 1

while low <= high:
    mid = (low + high) // 2

    if nums[mid] == target:
        print("Found at index:", mid)
        break

    # left half sorted
    if nums[low] <= nums[mid]:

        if nums[low] <= target <= nums[mid]:
            high = mid - 1
        else:
            low = mid + 1

    # right half sorted
    else:

        if nums[mid] <= target <= nums[high]:
            low = mid + 1
        else:
            high = mid - 1

