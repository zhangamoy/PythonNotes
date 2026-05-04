# # # # 函数和匿名函数

# # # 函数式编程

# # 过程式编程围绕控制块进行组织，关注控制流
# # 面向对象编程围绕类和对象组织，关注状态——特别是对象的属性
# # 函数式编程围绕函数进行组织
#     # 这种编程范式是声明式的，这意味着问题被分解为抽象步骤
#     # 需要为每个步骤编写一个函数，函数接受一个输入并产生一个输出
#     # 函数是自包含的，只做一件事，不关心其余部分
#     # 函数没有状态，不在调用之间存储信息
#     # 退出函数所有局部名称都会失效
#     # 相同输入调用函数时，总会生成相同的输出
#     # 函数不该有副作用，不改变任何东西
#     # 函数式编程的优势：不影响其它任何的情况下更改函数的实现方式
#     # 比紧密耦合的代码更容易重构和调试
# # python中的函数式编程是不纯的，这是可变数据类型存在所导致的
# # 函数式编程的规则：
#     # 每个函数都应该做一件特定的事情
#     # 一个函数的实现方式不应该影响程序中其他部分的行为
#     # 避免副作用！除非函数属于一个对象！
#     # 函数通常不该有状态或受外部状态的影响，相同的输入产生相同的输出
# # 误解：函数式编程可以避免循环
#     # 想法的初衷是避免处理控制流，所以递归通常优于手动循环
#     # 但不能总是避免循环，函数式编程不是万能药
#     # 并查集和哈希表，在纯函数式编程中无法有效实现
#     # 更应该将函数式编程范式的原则和概念融入编程风格

# # # 函数基础

# # 掷骰子：这是一个纯函数
# import random
# def roll_dice(sides):
#     return random.randint(1, sides)
# print("Roll for initiative...")
# player1 = roll_dice(20)
# player2 = roll_dice(20)
# if player1 >= player2:
#     print(f"Player 1 goes first (rolled {player1}).")
# else:
#     print(f"Player 2 goes first (rolled {player2}).")
# # 函数roll_dice()接收一个参数sides
# # 后面我们调用该函数并将值20作为实参传递
# # 并将两次函数调用返回的值绑定到player1和player2
# # 参数/parameter：函数定义中接收数据的插槽
# # 实参/argument：函数调用中传递给参数的数据

# # 一次掷多个骰子：返回元组
# import random
# def roll_dice(sides, dice):
#     return tuple(random.randint(1, sides) for _ in range(dice))
#     # 生成器表达式在后面详细介绍
# print("Roll for initiative...")
# player1, player2 = roll_dice(20, 2)
# if player1 >= player2:
#     print(f"Player 1 goes first (rolled {player1}).")
# else:
#     print(f"Player 2 goes first (rolled {player2}).")
# # 返回的元组可以被解包，即元组中的每一项被绑定到一个名称上
# # 左边列出的名称数量和元组中的值数量必须匹配

# # # 递归

# # 递归发生在函数调用自身时
# import random
# def roll_dice(sides, dice):
#     if dice < 1:
#         return ()
#     roll = random.randint(1, sides)
#     return (roll,) + roll_dice(sides, dice - 1)
# dice_cup=roll_dice(6,5)
# print(dice_cup)
# # 当dice=0时返回空元组，不再进行递归调用
# # 不这么做递归会尝试无限运行，虽然python会在某个时候停止程序
# # 递归深度：尚未返回的递归函数调用的数量，python将其限制在1000左右
# # 递归深度超出限制会引发RecursionError错误
# # 使用递归必须构建停止机制
# # 更改相关设置可实现更大的递归深度：
# import sys
# sys.setrecursionlimit(2000)

# # # 默认参数值

# # 如果只掷一次骰子，需要手动设定参数dice=1
# # (resualt,) = roll_dice(20, 1)
# # (resualt,)中的括号和逗号意味着元组中唯一元素的实际值被绑定到result上
# # 为了简化函数调用，给参数dice设定默认参数值
# import random
# def roll_dice(sides, dice=1):
#     return tuple(random.randint(1, sides) for _ in range(dice))
# (result,) = roll_dice(6)
# print(result)
# # 为参数指定默认参数值意味着定义了一个可选参数
# # 必须在可选参数之前列出所有必须参数

# # 默认参数值只在函数定义时计算一次
# def fibonacci_next(series=[1, 1]):
#     series.append(series[-1] + series[-2])
#     return series
# fib1 = fibonacci_next()
# print(fib1)
# fib1 = fibonacci_next(fib1)
# print(fib1)
# fib2 = fibonacci_next()
# print(fib2)  # 希望看到[1,1,2]，但却看到[1,1,2,3,5]
# # fib1、fib2实际上是series的两个别名，
# # 所以每次调用函数都会让series扩大一个元素
# def fibonacci_next(series=None):
#     if series is None:
#         series=[1,1]
#     series.append(series[-1] + series[-2])
#     return series
# fib1 = fibonacci_next()
# print(fib1)
# fib1 = fibonacci_next(fib1)
# print(fib1)
# fib2 = fibonacci_next()
# print(fib2)
# # 使用None作为默认参数值，在使用该值时创建了一个新的可变值

#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
