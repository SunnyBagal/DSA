def onesComplement(nums_str: str) -> str:
    res = ""
    for char in nums_str:
        if char == '0':
            res += '1'  
        else:
            res += '0'  
    return res

nums = "1010" 
print(onesComplement(nums))

