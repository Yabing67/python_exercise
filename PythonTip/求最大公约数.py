def find_gcd(a, b):
    # 在此处编写代码
    if a > b:
        a, b = b, a
    if a == 0:
        return b
    else:
        return find_gcd(a, b % a)


# 输入整数
# first_number = int(input())
# second_number = int(input())
first_number = 32
second_number = 8
# 调用函数
print(find_gcd(first_number, second_number))