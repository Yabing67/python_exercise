def string_match(a, b):
    count = 0
    if len(a) > len(b):
        a, b = b, a
    # i = 0
    # while i <= len(a) - 2:
    #     if a[i: i + 2] == b[i: i + 2]:
    #         count += 1
    #     i += 1
    for i in range(len(a) - 1):
        if a[i: i + 2] == b[i: i + 2]:
            count += 1
    return count

#输入数据
# a, b = eval(input())
a, b = 'xxcaazz', 'xxbaaz'
#调用函数打印结果
print(string_match(a, b))