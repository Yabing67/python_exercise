def hex_to_binary(hex_number):
    # 此处编写代码
    result = bin(hex_number)[2:]
    return f'{result:0>8}'

# 获取用户输入的16进制数
hex_number = int(input(), 16)

# 打印转换后的二进制数 
print(hex_to_binary(hex_number))

# 提示:
# 在函数hex_to_binary()中, 使用bin()函数将十六进制数转换为二进制数时，
# 会默认在结果前面加上0b表示这是一个二进制数。
# 因此, 在返回结果前需要去掉这个前缀。
