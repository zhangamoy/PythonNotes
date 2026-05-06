# ---------------------------------------------------------------------
# 问题 #
# 输入：含有若干数字的列表A，正整数n
# 输出：枚举A中元素构成的n位数组合，返回含有所有组合的排序列表
# 数字重复：同一个数字x出现m次，最终n位数中x最多出现m次
# 类型转换：A中如果有str/float形式储存的数字("5"、"5.0"、5.0)，转化为int
# 非法元素：所有不是0~9数字的元素(5.5、12、a、数、+)，需要剔除
# 结果验证：012不是合法的三位数，需要剔除；重复的数字，也需要剔除

# ---------------------------------------------------------------------
# 我的答案：不考虑数字重复，不考虑类型转化与非法输入，不考虑首位为零，指定n=3

# def digit_combinations():
#     source_list = [1, 2, 3, 4]
#     result_list = []
#     element = 0
#     source_list.sort
#     for i in source_list:
#         for j in source_list:
#             if i == j:
#                 continue
#             for k in source_list:
#                 if k == j or k == i:
#                     continue
#                 element = 100 * i + 10 * j + k
#                 result_list.append(element)
#     result_list.sort
#     return result_list

# def main():
#     result_list = digit_combinations()
#     print(result_list)

# main()

# ---------------------------------------------------------------------
# 参考1 @Gemini：用itertools.permutations实现组合

import itertools

A = [0, 1, 2, "2", 5.5, "apple", 11]
n = 3


def get_n_digit_combinations(A, n):
    # 1. 数据清洗
    cleaned_A = []
    for item in A:
        # 严格过滤：必须是 int 类型，或者是代表整数的字符串
        # 排除 float (5.5, 5.0) 和 非数字字符
        if isinstance(item, (int, str)):
            s_item = str(item)
            if s_item.isdigit():
                val = int(s_item)
                # 只保留 0-9 的单数字
                if 0 <= val <= 9:
                    cleaned_A.append(val)

    # 如果有效数字个数不足以构成 n 位数
    if len(cleaned_A) < n or n <= 0:
        return []

    # 2. 枚举并过滤
    unique_numbers = set()
    # itertools.permutations 自动处理“同一个数字出现 m 次”的约束
    for p in itertools.permutations(cleaned_A, n):
        # 剔除首位为 0 的情况（例如 n=3 时剔除 012）
        # 只有当 n 为 1 时，0 才可以出现在首位
        if p[0] == 0 and n > 1:
            continue

        # 将元组 (1, 0, 2) 转换为整数 102
        num_val = int("".join(map(str, p)))
        unique_numbers.add(num_val)

    # 3. 返回排序后的列表
    return sorted(list(unique_numbers))


# --- 测试 ---
# A 中包含重复数字、字符串、浮点数和非法字符
result = get_n_digit_combinations(A, n)
print(f"调用itertools模块, 生成的 {n} 位数: \n{result}")

# ---------------------------------------------------------------------
# 参考2 @Gemini：用递归函数实现itertools.permutations的效果


def get_n_digit_combinations_manual(A, n):
    # --- 第一步：依然是数据清洗 ---
    cleaned_A = []
    for item in A:
        s_item = str(item)
        if s_item.isdigit():
            val = int(s_item)
            if 0 <= val <= 9:
                cleaned_A.append(val)

    if len(cleaned_A) < n or n <= 0:
        return []

    results = set()  # 用来存储最终结果并去重

    # --- 第二步：核心递归函数 ---
    def backtrack(current_combination, remaining_indices):
        # 如果长度达到了 n，说明找到了一组排列
        if len(current_combination) == n:
            # 转换为整数并存入集合
            results.add(int("".join(map(str, current_combination))))
            return

        for i in range(len(remaining_indices)):
            idx = remaining_indices[i]
            val = cleaned_A[idx]

            # 剔除首位为 0 的情况：
            # 如果当前是第一个位置 (len=0) 且数字是 0，且 n > 1，则跳过
            if len(current_combination) == 0 and val == 0 and n > 1:
                continue

            # 递归：
            # 1. 把当前数字加入组合
            # 2. 把当前索引从“剩余可用索引”中剔除，传给下一层
            new_remaining = remaining_indices[:i] + remaining_indices[i + 1 :]
            backtrack(current_combination + [val], new_remaining)

    # 从空组合和全量索引开始递归
    initial_indices = list(range(len(cleaned_A)))
    backtrack([], initial_indices)

    return sorted(list(results))


# --- 测试 ---
# A 中包含重复数字、字符串、浮点数和非法字符
result = get_n_digit_combinations_manual(A, n)
print(f"调用手写递归函数, 生成的 {n} 位数: \n{result}")
