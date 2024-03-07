def check_string_compatibility(strings_list):
    # 此处编写代码
    # strings_list.sort(key=lambda x: len(x))
    strings_list.sort(key=len)
    pool = set(strings_list[-1])
    for string in strings_list[:-1]:
        if set(string).issubset(pool):
            continue
        else:
            return False
    return True


# 获取输入的字符串列表
# strings_list = input().split()
strings_list = "met fan manifest".split()
# 调用函数
print(check_string_compatibility(strings_list))
