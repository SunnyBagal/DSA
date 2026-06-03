strs = ["eat","tea","tan","ate","nat","bat"]

# ans = defaultdict(list)

# for s in strs:
#   key = "".join(sorted(s))
#   ans[key].append(s)

# print(list(ans.values()))


# from typing import List
# from collections import defaultdict

# class Solution:
#     def getSignature(self, s: str) -> str:
#         count = [0] * 26
#         for c in s:
#             count[ord(c) - ord('a')] += 1

#         result = []
#         for i in range(26):
#             if count[i] != 0:
#                 result.extend([chr(i + ord('a')), str(count[i])])

#         return ''.join(result)

#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         result = []
#         groups = defaultdict(list)

#         for s in strs:
#             groups[self.getSignature(s)].append(s)

#         result.extend(groups.values())

#         return result

res = {}

for word in strs:
    sorted_str = ''.join(sorted(word))
    print(sorted_str)
    if sorted_str not in res:
        res[sorted_str] = []
        print(res[sorted_str])

    res[sorted_str].append(word)

print(res)
print(list(res.values()))