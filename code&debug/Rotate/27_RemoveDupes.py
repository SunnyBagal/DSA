# Remove Duplicate from Sorted Array [in place], print the number of unique elements 

# first bring unique elements in the front(start), change iss array me hona chahiye

nums = [1, 1, 1, 2, 3, 4, 4, 7, 9, 9, 9, 10]
n = len(nums)
freq_map = {}

# Build frequency map and preserve order of first appearance
for i in range(n):
    if nums[i] not in freq_map:
        freq_map[nums[i]] = 1
    else:
        freq_map[nums[i]] += 1

# Overwrite nums with unique elements
j = 0
for k in freq_map:
    nums[j] = k
    j += 1

print(j)            # Number of unique elements
print(freq_map)     # Frequency map
print(nums[:j])     # Unique elements from original list


#______________________________-----------_____-----__---_--_-_-__-_-----_-_-_-_--_---_-__-_-_-__-

# optimal solution - 2pointers 

nums = [1,1,1,2,3,4,4,7,9,9,9,10]
#         |   | 
#         i   j  
#swap

def twoPointers(nums):
    n = len(nums)
    if n == 1:
        return 1 
    i = 0
    for j in range(1, n):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    return i + 1

# Example usage
length = twoPointers(nums)
print(length)          
print(nums[:length])   

