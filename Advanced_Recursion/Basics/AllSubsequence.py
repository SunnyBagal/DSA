nums = [9,5,7]
res = []

def solve(index, subset):
  if index >= len(nums):
    res.append(subset.copy())
    return 
  subset.append(nums[index])
  solve( index + 1, subset )
  subset.pop()
  solve( index + 1, subset )

solve(0, [])
print(res)

nums = [9,5,7]
res2 = []
def solve2(index, subset):
  if index >= len(nums):
    res2.append(subset.copy())
    return 
  subset.append(nums[index])
  solve2(index+1, subset)
  subset.pop()
  solve2(index+1, subset)

solve2(0, [])
print(res2)


def solve3(index, subset):
  if index >= len(nums):
    subset.append(subset.copy())
    return 
  subset.append(nums[index])
  solve3(index + 1, subset)
  subset.pop()
  solve3(index + 1, subset)

if(3rd Rep, dateAdd(Date Learned, 19, "days"), if(2nd Rep, dateAdd(Date Learned, 7, "days"), if(1st Rep, dateAdd(Date Learned, 1, "days"), dateAdd(Date Learned, 1, "days"))))