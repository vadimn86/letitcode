"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"
---
Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""


def common_prefix(strs):
    idx = 0
    prefix = ""
    while idx <= len(strs[0]):
        r = []
        for item in strs:
            r.append(item[: idx + 1])

        if all([r[0] == i for i in r]):
            prefix = r[0]
        else:
            break

        idx = idx + 1
    return prefix


if __name__ == "__main__":
    print(common_prefix(["flower", "flow", "flight"]))
