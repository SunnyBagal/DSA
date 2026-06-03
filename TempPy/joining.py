nums = [1,2,3]
sting_num = map(str,nums)
new = "".join(sting_num)
num = int(new)+1
digit_list = list(map(int, str(num)))
print(digit_list)
