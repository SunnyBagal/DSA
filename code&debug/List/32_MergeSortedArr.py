nums = [1,1,1,2,4,5,6]
nums2 = [1,2,3,6,7,8,9,10]
i = 0
j = 0
n = len(nums)
m = len(nums2)

res = []
while i < n and j < m:
    if nums[i] == nums2[j]:
        if not res or res[-1] != nums[i]:
            res.append(nums[i])
        i += 1
        j += 1

    elif nums[i] < nums2[j]:
        if not res or res[-1] != nums[i]:
            res.append(nums[i])
        i += 1

    else:
        if not res or res[-1] != nums2[j]:
            res.append(nums2[j])
        j += 1

while i < n:
    if res[-1] != nums[i]:
        res.append(nums[i])
    i += 1

while j < m:
    if res[-1] != nums2[j]:
        res.append(nums2[j])
    j += 1

print(res)