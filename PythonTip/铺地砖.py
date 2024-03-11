def make_bricks(small, big, goal):
    quotient = goal // 5
    rest = goal % 5
    if quotient <= big:
        if rest <= small:
            return True
        else:
            return False
    else:
        if (quotient - big) * 5 + rest <= small:
            return True
        else:
            return False

#输入数据
# small, big, goal = eval(input())
small, big, goal = 3, 1, 8
#调用函数打印结果
print(make_bricks(small, big, goal))