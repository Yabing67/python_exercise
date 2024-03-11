def xyz_there(str):
    # 遍历字符串，检查每个"xyz"的位置
    for i in range(len(str) - 2):
        if str[i:i + 3] == 'xyz':
            # 如果前一个字符不是"."，则返回True
            if i == 0 or str[i - 1] != '.':
                return True

    # 如果没有满足条件的"xyz"，返回False
    return False
#输入数据
str = eval(input())
#调用函数打印结果
print(xyz_there(str))
