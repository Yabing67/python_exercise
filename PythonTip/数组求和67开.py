def sum67(nums):
    # 定义标志变量，用于指示是否处于忽略区域
    ignore = False
    total_sum = 0

    for num in nums:
        if num == 6:
            ignore = True
        elif num == 7 and ignore:
            ignore = False
        elif not ignore:
            total_sum += num

    return total_sum

#输入数据
nums = eval(input())
#调用函数打印结果
print(sum67(nums))

# 该函数遍历数组，当遇到数字6时，将标志变量ignore设置为True，表示进入忽略区域。当在忽略区域内遇到数字7时，将ignore重新设置为False，
# 表示忽略区域结束。在不在忽略区域内时，将数字累加
