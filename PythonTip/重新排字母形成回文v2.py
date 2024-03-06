def can_form_palindrome(word):
    # 统计每个字母出现的次数
    char_count = {}
    for char in word:
        char_count[char] = char_count.get(char, 0) + 1

    # 回文单词的特点是最多只有一个字母出现的次数为奇数
    odd_count = 0
    for count in char_count.values():
        if count % 2 != 0:
            odd_count += 1

    # 如果奇数次的字母超过一个，则无法形成回文
    return odd_count <= 1

# 测试
word = "sarars"
result = can_form_palindrome(word)
print(result)
