nums = [10,11,11,12,12,13,13,13,1,2,3,4]
target = 11

def isThere(num, target):
    n = len(num)
    low = 0
    high = n - 1  

    while low <= high:
        mid = (low + high) // 2

        if num[mid] == target:
            return True
        
        if num[low] == num[mid] == num[high]:
            low += 1
            high -= 1
            continue
        
        if num[low] <= num[mid]:   # left sorted
            if num[low] <= target <= num[mid]:
                high = mid - 1
            else:
                low = mid + 1

        else:                      # right sorted
            if num[mid] <= target <= num[high]:
                low = mid + 1
            else:
                high = mid - 1

    return False


print(isThere(nums, target))