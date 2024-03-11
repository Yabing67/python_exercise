def count_consecutive_ones(input_list):
    # 此处编写代码
    consecutive_ones_count = 0
    current_ones_count = 0

    for digit in input_list:
        if digit == 1:
            current_ones_count += 1
        else:
            if current_ones_count > 1:
                consecutive_ones_count += 1
            current_ones_count = 0

    # Check for consecutive ones at the end of the list
    if current_ones_count > 1:
        consecutive_ones_count += 1

    return consecutive_ones_count


# 获取输入, 转换为列表
input_list = list(map(int, input().split()))
# 调用函数
print(count_consecutive_ones(input_list))