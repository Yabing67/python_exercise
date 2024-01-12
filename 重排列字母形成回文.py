from collections import Counter


def can_form_palindrome(word):
    # 在此处编写你的代码
    length = len(word)
    cnt = Counter(word)
    if length % 2 == 0:
        for i in cnt.values():
            if i % 2 != 0:
                return False
        return True
    else:
        count1 = 0
        count2 = 0
        for i in cnt.values():
            if i % 2 != 0:
                count1 += 1
            elif i % 2 == 0:
                count2 += 1
        if count1 == 1:
            return True
        else:
            return False


# 从用户处获取输入
# word = input()
word = "sarars"
# 调用函数
print(can_form_palindrome(word))