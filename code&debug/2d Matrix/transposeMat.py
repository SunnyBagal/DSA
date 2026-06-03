nums = [[5,9,1],[2,3,7]]

rows = len(nums)
col = len(nums[0])

res = [[0]*rows  for _ in range(col)]
print(res) 

for i in range(rows):
  for j in range(col):
    res[j][i] = nums[i][j]

print(res)