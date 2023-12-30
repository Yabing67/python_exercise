def find_unique(lst):
    # 此处编写代码
    dic = {}
    for i in lst:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    result = []
    for k, v in dic.items():
        if v == 1:
            result.append(k)
    return result

# 获取用户输入并转为数字列表
# numbers = list(map(int, input().split()))
numbers = "1 2 2 3 4 4 5 5"

# 调用函数
print(find_unique(numbers))