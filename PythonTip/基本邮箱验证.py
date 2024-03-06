def is_email_valid(email):
    # 此处编写代码
    if "@" not in email:
        return False
    elif "." not in email:
        return False
    else:
        index = email.find("@")
        if index == 0:
            return False
        elif "." not in email[index + 2:]:
            return False
        else:
            return True


# 获取输入
# email = input()
email = "user@website.com"

# 调用函数
print(is_email_valid(email))