tokens = ["2","1","+","3","*"]
n = len(tokens)
res = []

for i in tokens:
  if i not in '/*+-':
    res.append(int(i))
  else:
    a = res.pop()
    b = res.pop()

    if i == '+': 
      res.append(a+b)
    elif i == '-':
      res.append(a-b)
    elif i == '*':
      res.append(a*b)
    else:
      res.append(b/a)

print(res[0])

