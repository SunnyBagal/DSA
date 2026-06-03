s = 'leet**cod*e'
my_list = list(s)
print(my_list, '\n')
n = len(s)
i = 0
while i < len(my_list):
    if my_list[i] == '*':
        if i > 0:
          my_list = my_list[:i-1] + my_list[i+1:]
          i -= 1
        else:
          my_list = my_list[i+1:]
    else:
        i += 1

print(my_list)


stack = []

for i in s:
    if i == '*':
        if stack :
            stack.pop()

    else:
        stack.append(i)

print(stack)