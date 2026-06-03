#Move zeroes to the end

# nums = [1, 0, 2, 4, 3, 0, 0, 3, 5, 1]
# temp = []
# n = len(nums)


# for i in range(n):
#     if nums[i] != 0:
#         temp.append(nums[i])

# k = len(temp)

# for i in range(0, k):
#     nums[i] = temp[i]

# for i in range(k, n):
#     nums[i] = 0

# print(nums)



#-----------------------------------------------------------------------------

# Optimal Solution 

def opSol(nums):
    n = len(nums)
    
    pos = 0  
    for i in range(n):
        if nums[i] != 0:
            nums[pos], nums[i] = nums[i], nums[pos]
            pos += 1

    return nums

nums = [0, 0, 2, 4, 3, 0, 0, 3, 5, 1]
new = opSol(nums)
print(new)
