# nums = [2,2,2,2,2]
# target = 8
# my_set = set()
# n = len(nums)
# for i in range(n):
#   for j in range(i + 1, n):
#     for k in range(j + 1, n):
#       for l in range(k + 1, n ):
#         if nums[i] + nums[j] + nums[k] + nums[l] == target:
#           temp = [nums[i] , nums[j] , nums[k] , nums[l]]
#           temp.sort()
#           my_set.add(tuple(temp))

# print(my_set)

#~ TC : O(N^4)
#~ SC : O(N)

# nums = [1,0,-1,5,-2,2,0,9]
# target = 0
# n = len(nums)

# my_set = set()

# for i in range(n):
#     for j in range(i+1, n):
#         hash_set = set()

#         for k in range(j+1, n):
#             fourth = target - (nums[i] + nums[j] + nums[k])

#             if fourth in hash_set:
#                 temp = [nums[i], nums[j], nums[k], fourth]
#                 temp.sort()
#                 my_set.add(tuple(temp))

#             hash_set.add(nums[k])

# print(my_set)

#~ TC : O(n³)
#~ SC : O(n)



nums = [1,1,1,2,2,3,3,4]
nums.sort()

n = len(nums)
ans = []
target = 8

for i in range(n):
    if i > 0 and nums[i] == nums[i-1]:
        continue

    for j in range(i+1, n):
        if j > i+1 and nums[j] == nums[j-1]:
            continue

        k = j + 1
        l = n - 1

        while k < l:
            total_sum = nums[i] + nums[j] + nums[k] + nums[l]

            if total_sum < target:
                k += 1
            elif total_sum > target:
                l -= 1
            else:
                ans.append([nums[i], nums[j], nums[k], nums[l]])
                k += 1
                l -= 1

                while k < l and nums[k] == nums[k-1]:
                    k += 1
                while k < l and nums[l] == nums[l+1]:
                    l -= 1
            
print(ans)

#~ Time:  O(n³)
#~ Space: O(1) (excluding output)



