# Prestoring value in some datastructure like List/Dic/Set and then fetching it

nArr = [5,3,2,2,1,5,5,7,5,10]
mArr = [10,111,1,9,5,67,2]

# for nums in m:
#   count = 0
#   for x in n:
#     if x == nums:
#       count += 1
#   print(count)

#~ TC: O(N x M)
#~ SC: O(1).  

##############################*


nArr = [5,3,2,2,1,5,5,7,5,10]
mArr = [10,111,1,9,5,67,2]

hash_map = {}
n = len(nArr)
m = len(mArr)

for i in range( n):
  hash_map[nArr[i]] = hash_map.get(nArr[i], 0) + 1

for num in mArr:
    print(hash_map.get(num, 0), end=" ")

# for j in range(m):
#   if mArr[j] in hash_map:
#     print(hash_map[mArr[j]], end=" ")
#   else:
#     print(0, end=" ")
 


