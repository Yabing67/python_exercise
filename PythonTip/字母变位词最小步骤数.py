from collections import Counter


def min_removals_to_anagram(str1, str2):
    # 此处编写代码
    cnt1 = Counter(str1)
    cnt2 = Counter(str2)
    cnt = cnt1 - (cnt1 & cnt2) + cnt2 - (cnt1 & cnt2)
    return len(list(cnt.elements()))


# 获取输入
# str1 = input()
str1 = "cab"
# str2 = input()
str2 = "base"

# 调用函数，输出结果
print(min_removals_to_anagram(str1, str2))