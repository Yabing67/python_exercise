def array123(nums):
    string = "".join(str(num) for num in nums)
    if "123" in string:
        return True
    return False

#输入数据
# nums = eval(input())
nums = [1, 1, 2, 3, 1]
#调用函数打印结果
print(array123(nums))