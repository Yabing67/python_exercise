def is_heterogram(s):
    # 此处编写代码
    s = s.replace(" ", "")
    if len(set(s)) == len(s):
        return "No"
    else:
        return "Yes"

# 获取输入
# input_string = input()
input_string = "hello world"

# 调用函数，输出结果
print(is_heterogram(input_string))