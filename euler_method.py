def euler_method(nodes_num:int, start:float, end:float, init_value:float, fn:callable):
    # 默认所有输入数据都是合法的
    
    # 计算步长
    h = (end - start) / nodes_num
    # 定义点列
    points = [start + i*h for i in range(nodes_num)]
    values = [0 for _ in range(nodes_num)]
    
    # 开始迭代计算values
    index = 1
    values[0] = init_value
    while index < nodes_num:
        values[index] = values[index - 1] + h * fn(points[index - 1], values[index - 1])
        index += 1
    return values

fn = lambda x,y: x*y

results = euler_method(100, 0, 1, 1, lambda x,y: x+y)
print(results)