def check_double_base_palindrome(number):
    # 此处编写代码
    flag_oct = False
    if str(number)[::-1] == str(number):
        flag_oct = True

    flag_bin = False
    number_bin = bin(number)[2:]
    if number_bin == number_bin[::-1]:
        flag_bin = True

    if flag_bin and flag_oct:
        return True
    else:
        return False
# 获取用户输入
# number = int(input())
number = 313

# 调用函数
print(check_double_base_palindrome(number))