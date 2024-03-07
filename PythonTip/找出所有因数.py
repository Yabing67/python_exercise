def find_factors(number):
    factors = []
    # 特殊处理 1
    factors.append(1)
    # 遍历从 2 到 sqrt(number) 的所有数字
    i = 2
    while i * i <= number:
        # 如果 number 能够整除 i，则 i 和 number/i 都是 number 的因数
        if number % i == 0:
            factors.append(i)
            if number // i != i:
                factors.append(number // i)
        i += 1
    factors.append(number)
    # 对因数列表进行排序并返回
    return sorted(factors)

# 示例输入
number = 16
# 调用函数并打印结果
print("Factors of", number, "are:", find_factors(number))
