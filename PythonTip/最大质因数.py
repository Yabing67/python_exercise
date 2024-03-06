def largest_prime_factor(num):
    # 此处编写代码
    result = []
    for i in range(2, num):
        if num % i == 0:
            result.append(i)

    largest_prime_factor = min(result)
    for i in result:
        if is_prime(i) and i > largest_prime_factor:
            largest_prime_factor = i
    return largest_prime_factor


def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

# 获取输入数字
# user_input = int(input())
user_input = 1267

# 调用函数
print(largest_prime_factor(user_input))
