def smallest_number(number, k):
    # 将数字转换为字符串，以便逐字符处理
    num_str = str(number)
    stack = []

    for digit in num_str:
        # 当栈不为空，且栈顶元素大于当前元素，且还需要删除更多数字时
        while k > 0 and stack and stack[-1] > digit:
            stack.pop()
            k -= 1
        stack.append(digit)

    # 如果还需要删除更多数字，从尾部删除
    final_number = stack[:-k] if k else stack

    # 将栈中的元素组合成字符串，转换为整数
    return int("".join(final_number))


# 示例
number = 7896
k = 2
print(smallest_number(number, k))
