# 使用json模块解析输入并处理JSON数据
import json

def map_list_dict(input_dict, input_list):
    # 在这里编写你的代码
    result = {}
    items = list(input_dict.items())
    for i, k in enumerate(input_list):
        keys = list(input_dict.keys())
        dict = {keys[i]: input_dict[keys[i]]}
        result[k] = dict
    return result

# 获取输入字符串并将其解析为json
# input_str = '{"a": 1, "b": 2, "c": 3} 6 7 8'
# input_dict = json.loads(input_str)
input_dict = json.loads(input())
# 获取整数输入并将其转换为列表
input_list = list(map(int, input().split()))
# 调用函数
print(map_list_dict(input_dict, input_list))