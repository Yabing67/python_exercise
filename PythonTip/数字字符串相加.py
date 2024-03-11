def add_numbers(num1, num2):
    # 此处编写代码
    if num1 == "" or num1 == "None":
        return "Invalid Operation"
    elif num2 == "" or num2 == "None":
        return "Invalid Operation"
    else:
        return str(int(num1) + int(num2))
# 获取用户输入num1 和 num2
num1 = input()
num2 = input()

# 调用函数
result = add_numbers(num1, num2)

# 打印和
print(result)