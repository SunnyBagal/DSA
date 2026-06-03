nums = [73, 74, 75, 71, 69, 72, 76, 73]
#        0   1.  2.  3.  4.  5.  6.  7

res = []

for i in range(len(nums)):
    found = False
    for j in range(i+1, len(nums)):
        if nums[i] < nums[j]:
            res.append(j - i)
            found = True
            break
    if not found:
        res.append(0)
print(res)


def dailyTemperatures(nums):
    res = [0] * len(nums)
    stack = []  # stores indices

    for i in range(len(nums)):
        while stack and nums[i] > nums[stack[-1]]:
            prev = stack.pop()
            res[prev] = i - prev
        stack.append(i)

    return res

print(dailyTemperatures(nums))