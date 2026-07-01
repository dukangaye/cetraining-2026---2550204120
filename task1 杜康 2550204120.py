"""
统计文本文件中每个单词出现次数的函数
"""

import re
from collections import Counter


def count_words(filepath):
    """
    读取文本文件，统计每个单词出现的次数。

    参数:
        filepath: 文本文件的路径

    返回:
        dict: 单词 → 出现次数的映射，按次数降序排列
    """
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            text = f.read()
    except FileNotFoundError:
        print(f"✗ 文件不存在: {filepath}")
        return {}
    except Exception as e:
        print(f"✗ 读取文件出错: {e}")
        return {}

    # 用正则提取所有英文单词（忽略大小写差异，统一转小写）
    words = re.findall(r"[a-zA-Z]+", text.lower())

    # 统计词频并按次数降序排列
    word_count = Counter(words)
    return dict(word_count.most_common())



    """
    格式化输出词频统计结果。

    参数:
        word_count: count_words() 返回的字典
        top_n:     仅显示前 N 个，None 表示全部显示
    """
    if not word_count:
        print("未统计到任何单词。")
        return

    items = list(word_count.items())
    if top_n:
        items = items[:top_n]

    print(f"\n{'排名':<6}{'单词':<20}{'次数':<8}")
    print("-" * 34)
    for rank, (word, count) in enumerate(items, 1):
        print(f"{rank:<6}{word:<20}{count:<8}")


if __name__ == "__main__":
    # 示例：统计 sample.txt 中的词频
    result = count_words("sample.txt")
    print_word_count(result, top_n=10)  # 只显示前 10 个