nums = [3, 9, 5, 6, 7, 2, 1]
k = 3 
n = len(nums)
# rotation = k % n
# for i in range(rotation):
#     e = nums.pop()       # remove from end
#     nums.insert(0, e)    # insert at beginning

# print(nums)


#-------------------------------------------------#-------------------------------------------------#
k = 3 
n = len(nums)
k = k % n
nums[:] = nums[n-k:] + nums[:n-k]
# print(nums)


#-------------------------------------------------#-------------------------------------------------#

def reverse(nums, left, right):
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1


def rotate(nums, k):
    n = len(nums)
    reverse(nums, 0, k-1)
    reverse(nums, k, n-1)
    reverse(nums, 0, n-1)
    return nums


nums = [1,2,3,4,5,6,7,8] 
print(rotate(nums, 3))
# print(nums)


