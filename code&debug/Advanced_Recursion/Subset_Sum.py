nums = [5,9,3]

res = []
def solve(index, total):
  if index >= len(nums):
    res.append(total)
    return

  sum = total + nums[index]
  solve(index + 1, sum) 
  sum = total
  solve(index + 1, sum)

solve(0, 0)

print(res)