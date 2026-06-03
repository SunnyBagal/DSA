def Selection_Sort(nums):
  n = len(nums)

  for i in range(n):
    min_index = i
    for j in range(i+1, n):
      if nums[j] < nums[min_index]:
        min_index = j
    nums[i], nums[min_index] = nums[min_index], nums[i]
  return nums

n = [1,7,8,4,5,6,9,2]
print(Selection_Sort(n))