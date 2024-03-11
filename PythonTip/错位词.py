def are_anagrams(string1, string2):
    # 此处编写代码
    string1 = string1.replace(" ", "")
    string2 = string2.replace(" ", "")
    if set(string1.lower()) == set(string2.lower()) and string1 != string2:
        return True
    else:
        return False


# 获取输入string1 和 string2
string1 = "Astronomer"
string2 = "Moon starer"
# 调用函数并打印结果
print(are_anagrams(string1, string2))
