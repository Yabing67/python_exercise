def digit_sort(numbers):
    # 定义一个自定义的排序函数，根据数字的位数和数字本身进行排序， 可以包含多个排序标准
    # 确保按照位数从高到低以及相同位数的数字按照升序排序
    def custom_sort(num):
        return -len(str(num)), num

    # 使用自定义排序函数对数字列表进行排序
    sorted_numbers = sorted(numbers, key=custom_sort)

    return sorted_numbers


# 示例输入
numbers = [101, 2, 678, 45, 3, 87]
# 调用函数并打印结果
print(digit_sort(numbers))
