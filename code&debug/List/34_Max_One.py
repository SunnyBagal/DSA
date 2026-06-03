num = [1,1,0,1,0,1,1,1,1,0,1,1,1,1,1]
count = 0
max_count = 0
for x in num:
    if x == 1:
        count += 1
        max_count = max(max_count, count)
    else:
        count = 0
print(f'The maximum number of ones are: {max_count}')