def count_duplicate_chars(input_string):
    # 在此处编写你的代码
    dic = {}
    for i in input_string:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    count = 0
    for v in dic.values():
        if v == 1:
            continue
        else:
            count += 1
    return count
# 获取用户输入
# test_string = input()
test_string = "Programming"

# 调用函数
result = count_duplicate_chars(test_string)
print(result)