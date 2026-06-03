
#* SET MATRIX ZEROS

mat = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
rows = len(mat)
cols = len(mat[0])

# first pass: record which rows and columns should be zeroed
zero_rows = set()
zero_cols = set()


for i in range(rows,):
    for j in range(cols):
        if mat[i][j] == 0:
            zero_rows.add(i)
            zero_cols.add(j)
            
print(zero_rows, zero_cols)
# second pass: set appropriate cells to 0 without altering structure mid-iteration
for i in range(rows):
    for j in range(cols):
        if i in zero_rows or j in zero_cols:
            mat[i][j] = 0

print(mat)

