nums = [4,5,6,7,1,2]
n = len(nums)
low = 0
high = n - 1
mini = nums[low]
while low <= high:
    mid = (low + high) // 2

    if nums[mid] < nums[high]:
        mini = min(mini, nums[mid])
        high = mid - 1

    else:
        mini = min(mini, nums[low])
        low = mid + 1

print(mini)

#~ TC: O(log N)
#~ SC: O(1)