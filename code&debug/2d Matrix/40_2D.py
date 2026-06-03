nums = [[5,10,8], [7,6,3],[2,1,9]]

rows = len(nums)
col = len(nums[0])

# for i in range(rows):
#   for j in range(col):
#     print(nums[i][j])


#*-----------------------------#----------------------------------------#-------------------------------------#

#~ Print Upper Triangle:
#&    5  7  8
#&    *  6  3
#&.   *  *  9

for i in range(rows):
  for j in range(col):
    if j >= i:
      print(nums[i][j], end=" ")
    else: 
      print('*', end=" ")
  print()
print()

#*-----------------------------#----------------------------------------#-------------------------------------#

#~ Print Lower Triangle:
#&    5  *  *
#&    7  6  *
#&.   2  1  9

for i in range(rows):
  for j in range(col):
    if i >= j:
      print(nums[i][j],end=" ")
    else:
      print('*',end=" ")
  print()


print()
#*-----------------------------#----------------------------------------#-------------------------------------#

#~ Print Diagonal Triangle:
#&    *  7  8
#&    7  *  3
#&.   2  1  *

for i in range(rows):
  for j in range(col):
    if i == j:
      print('*',end=" ")
    else:
      print(nums[i][j],end=" ")
  print()