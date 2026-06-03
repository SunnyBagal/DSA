nums = [-1,0,1,2,-1,-4]
n = len(nums)
# my_set = set()

# for i in range(n):
#   for j in range(i+1, n):
#     for k in range(j+1, n):
#       if nums[i] + nums[j] + nums[k] == 0:
#         temp = [nums[i], nums[j], nums[k]]
#         temp.sort()
#         my_set.add(tuple(temp))

# print([list(ans) for ans in my_set])

my_set = set()
result = set()
for i in range(n):
  for j in range(i+1, n):
    
    third = -(nums[i] + nums[j])
    if third in my_set:
      temp = [nums[i], nums[j], third]
      temp.sort()
      result.add(tuple(temp))
    my_set.add(nums[j])

print([list(ans) for ans in result])