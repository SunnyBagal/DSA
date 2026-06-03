nums = [7,6,8,6,1,1]
res = []
while len(nums) > 1:
    left_sum = nums[0] + nums[1]
    right_sum = nums[-1] + nums[-2]

    if left_sum < right_sum:
        nums = [left_sum] + nums[2:]
        res.append(left_sum)
        print(nums, ", res =", [left_sum])
    else:
        nums = nums[:-2] + [right_sum]
        res.append(right_sum)
        print(nums, ", res =", [right_sum])

print(nums)
print(sum(res))