def is_title(sentence):
    # 在此处编写代码
    word_ls = sentence.split()
    for i in word_ls:
        if i != i.capitalize():
            return False
    return True


# 从用户处获取输入
# input_sentence = input()
input_sentence = "The Quick Brown Fox"

# 调用函数
print(is_title(input_sentence))