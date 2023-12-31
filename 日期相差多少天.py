import datetime

def calculate_days_between(date1, date2):
    # 在此处编写你的代码
    datetime1 = datetime.datetime.strptime(date1, "%Y-%m-%d")
    datetime2 = datetime.datetime.strptime(date2, "%Y-%m-%d")
    days = datetime2 - datetime1
    return days.days

# 获取用户输入
date1 = input()
date2 = input()

# 调用函数
print(calculate_days_between(date1, date2))