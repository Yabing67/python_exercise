def sum_of_digits_in_factorial(num):
    # 在此处编写你的代码
    if num == 0:
        return 1
    product = 1
    i = 1
    while i <= num:
        product *= i
        i += 1

    result = 0
    while product // 10 != 0:
        product = product // 10
        result += product % 10
    return result


# 获取用户输入
# num = int(input())
num = 0

# 调用函数
print(sum_of_digits_in_factorial(num))