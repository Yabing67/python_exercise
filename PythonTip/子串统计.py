def last2(str):
    # 获取倒数第二个字符组成的子串
    last2_chars = str[-2:]
    count = 0

    # 遍历字符串，比较每个位置的后两个字符与目标子串是否相等
    for i in range(len(str) - 2):
        if str[i:i + 2] == last2_chars:
            count += 1

    return count
    # return str.count(str[-2:], 0, len(str) - 2)


#输入数据
# str = eval(input())
# str = "axxxaaxx"
str = "axxxxxxx"
#调用函数打印结果
print(last2(str))
