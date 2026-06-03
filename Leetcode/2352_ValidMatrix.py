arr = [[3,2,1],[1,7,6],[2,7,7]]

s = {tuple(sub) for sub in arr}

# transpose
result = list(zip(*arr))  # gives tuples directly

for col in result:
    print(col in s)