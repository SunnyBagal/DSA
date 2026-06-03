nums = [5, -2, 3, 9, 0, 6, 10, 7]
n = len(nums)
temp = nums[n-1]

for i in range(n-2,-1,-1):
    nums[i+1] = nums[i]
nums[0] = temp
print(nums)


# TC : O(N-1)
# SC : O(1)