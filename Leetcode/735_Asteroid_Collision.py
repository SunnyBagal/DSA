nums = [3,5,-6,2,-1,4]
n = 0
res = [nums[0]]

for i in range(1,len(nums)):

  if nums[i] > res[n] :
    res.append(nums[i])
    n += 1
  elif nums[i] < res[n] and abs(nums[i]) > res[n]:
    res.pop()
    res.append(nums[i])
print(res)