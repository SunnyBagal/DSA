matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
rows = len(matrix)
cols = len(matrix[0])

for i in range(rows): 
    for j in range(i + 1, cols):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

# 2. Reverse each row using a manual swap loop (no .reverse() function)
for i in range(rows):
    # This is the "Two-Pointer" swap logic we discussed
    for j in range(cols // 2):
        # Swap start and end of the row
        matrix[i][j], matrix[i][cols - 1 - j] = matrix[i][cols - 1 - j], matrix[i][j]

print(matrix)