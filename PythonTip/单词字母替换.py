def shift_char(word):
    # 此处编写你的代码
    result = ""
    for i in word:
        if i.islower():
            i = chr((ord(i) - 97 + 1) % 26 + 97)
        elif i.isupper():
            i = chr((ord(i) - 65 + 1) % 26 + 65)
        result += i
    return result

# 获取单词
word = input()
# 调用函数
print(shift_char(word))