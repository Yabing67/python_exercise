def reverse_number_digits(num):
    # 在此处编写你的代码
    reversed_ls = []
    while num > 0:
        reversed_ls.append(num % 10)
        num = num // 10
        if num == 0:
            break
    return reversed_ls


# 获取用户输入
num = int(input())

# 调用函数
print(reverse_number_digits(num))