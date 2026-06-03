nums = [1,99,101,98,2,5,3,100,1,1]
n = len(nums)
max_count = 0

#! Brute Force

for i in range(n):
  num = nums[i]
  count = 1
  while num + 1 in nums:
    count += 1
    num = num + 1
  max_count = max(max_count, count)

print(max_count)

#! TC: O(N^2)
#! SC: O(1)

#* Optimal Solution:

nums = [1,99,101,98,2,5,3,100,1,1]
n = len(nums)
my_set = set()
for i in range(n):
    my_set.add(nums[i])
longest = 0
for num in my_set:
    if num-1 not in my_set:
        x = num
        count = 1
        while x+1 in my_set:
            count += 1
            x = x+1
        longest = max(longest, count)
print(longest)


#~ TC: O(3N)
#~ SC: O(N)