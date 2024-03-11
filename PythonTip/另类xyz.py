def xyz_there(str):
    if str.count("xyz") == 0:
        return False
    else:
        for i in range(str.count("xyz")):
            index = str.find("xyz")
            if index == 0:
                return True
            else:
                if str[index - 1] == ".":
                    str = str[index + 2:]
                    continue
                else:
                    return True
        return False
#输入数据
# str = eval(input())
str = 'abc.xyzxyz'
#调用函数打印结果
print(xyz_there(str))
