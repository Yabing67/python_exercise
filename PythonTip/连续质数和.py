def is_prime(n):
    """检查一个数是否为质数。"""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_consecutive_prime_sum(limit):
    # 生成小于limit的质数列表
    primes = [n for n in range(2, limit) if is_prime(n)]
    # 找到连续质数和小于limit的最长列表
    max_length = 0
    max_sum = 0
    for i in range(len(primes)):
        for j in range(i + max_length, len(primes)):
            prime_sum = sum(primes[i:j])
            if prime_sum < limit:
                if is_prime(prime_sum) and (j - i) > max_length:
                    max_length = j - i
                    max_sum = prime_sum
            else:
                # 如果当前的和已经超过了限制，就不需要继续增加质数
                break
    return max_sum

# 示例输入
limit = 100
# 调用函数并打印结果
print(find_consecutive_prime_sum(limit))
