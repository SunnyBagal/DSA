nums = [55,32,-97,99,3,67]
largest = float('-inf')
for i in range(len(nums)):
  # if nums[i] > largest:
  #   largest = nums[i]
  largest = max(nums[i],largest)

print(largest)