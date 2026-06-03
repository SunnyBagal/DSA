def toNum (string):
  res = 0
  for numbers in string:
    res *= 10
    res += int(numbers)
  return res

my_str = '123.5'
print(toNum(my_str)) 