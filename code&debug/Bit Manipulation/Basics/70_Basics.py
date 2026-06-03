def convert2Binary(nums: int) -> str:
    if nums == 0:
        return "0"
    res = ""
    while nums > 0:
        if nums % 2 == 1:
            res += "1"
        else:
            res += "0"
        nums = nums // 2
    res = res[::-1]
    return res


def convert2Integer(binary_str: str) -> int:
    reversed_bin = binary_str[::-1]

    res = 0
    for i in range(len(reversed_bin)):
        current_value = int(reversed_bin[i]) * (2**i)
        res = res + current_value
    return res

num = 12
binary_result = convert2Binary(num)
print(binary_result)
print(convert2Integer(binary_result))