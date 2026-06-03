num = [1,6,4,3,2,5,7,0,1]
flag = 0
for i in range(len(num)+1) : 
  if i in num:
    flag = 1
  else:
    print(i)

#~ TC: O(N^2)
#~ SC: O(1)

# nums = [9,6,4,3,2,5,7,0,1]
# n = len(nums)
# freq_map = {}
# for i in range(0, n+1):
#   freq_map[i] = 0
# print(freq_map)

# for j in nums: 
#   freq_map[j] += 1
# for k,v in freq_map.items():
#   if v == 0:
#     print(k)
# print(freq_map)


# act_sum = n*(n+1)*1/2
# wegot = sum(nums)
# mis_val = act_sum - wegot
# print(int(mis_val))
