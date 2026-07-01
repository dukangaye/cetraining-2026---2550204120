def calculate_average(numbers):
    """
    计算列表的平均值。

    参数:
        numbers (list): 包含数字的列表（int 或 float）

    返回:
        float: 列表的平均值。如果列表为空，返回 None。

    示例:
        >>> calculate_average([1, 2, 3, 4, 5])
        3.0
        >>> calculate_average([])
        None
    """
    if not numbers:
        return None
    return sum(numbers) / len(numbers)


# 测试示例
if __name__ == "__main__":
    # 正常情况
    print(calculate_average([1, 2, 3, 4, 5]))  # 输出: 3.0

    # 浮点数列表
    print(calculate_average([1.5, 2.5, 3.0]))  # 输出: 2.333...

    # 空列表
    print(calculate_average([]))  # 输出: None

    # 单元素列表
    print(calculate_average([42]))  # 输出: 42.0