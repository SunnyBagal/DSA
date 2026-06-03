
n = 5873
num = n

while num > 0:
  last_digit = num % 10
  print(last_digit, end='')
  num = num // 10
