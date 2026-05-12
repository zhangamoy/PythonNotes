# # # # 生成器和推导式 # # # #

# 生成器表达式 ，允许在一个语句中重写循环的整个逻辑


# --------------------------------------------------------------------------------------------
# # # 惰性求值和贪婪迭代

# # 惰性求值
# # 这个过程中，迭代器在被请求之前不提供下一个值
# # 该行为，再加上迭代器不关心其可迭代对象中可能有多少项的事实
# # ？构成了生成器对象强大功能的基础

# # 贪婪迭代
# # 迭代器是惰性的，可迭代对象则不是！
# # 错误地定义一个可迭代对象将导致程序锁死在无限循环中
# # 某些情况下，遍历所有可用的系统内存可能引发 MemoryError

# # 案例：困
# import time
# sleepy = ["no pause", time.sleep(1), time.sleep(2)]  # ...three second pause...
# print(sleepy[0])
# # python 在将列表分配给 sleepy 之前，就急切地对每一个表达式进行了评估
# # 即，调用了 time.sleep() 两次

# # 当处理大量数据或特别复杂的表达式时，集合可能称为性能瓶颈
# # 因此，处理大量数据的最佳方法就是使用生成器或生成器表达式！


# --------------------------------------------------------------------------------------------
# # # 无限迭代器

# # 惰性求值使无限迭代器成为可能，
# # 这样就可以 # 按需 # 提供值且值不会被耗尽
# # itertools 模块提供三种无限迭代器
# # count() 从给定数值开始计数，每次加上可选的步长值
# # cycle() 循环遍历可迭代对象中的每个元素
# # repeat() 重复给定的值（可指定重复次数）
# # 它们没有刹车，非常危险：
# # for 循环中，需要人为设定 break 语句
# # 使用星号表达式解包或创建集合时，python 解释器会锁定甚至崩溃


# --------------------------------------------------------------------------------------------
# # # 生成器

# # 生成器函数是迭代器类的替代品
# # 直接调用生成器函数时返回一个生成器迭代器（又称生成器对象）
# # 该迭代器封装了生成器函数套件中的逻辑
# # 案例：车牌号生成

# from itertools import product
# from string import ascii_uppercase as alphabet


# def gen_license_plates():
#     for letters in product(alphabet, repeat=3):
#         # 使用 product 迭代器（笛卡尔积）遍历所有字母组合
#         # 等价于 product(alphabet, alphabet, alphabet)
#         # 其中，alphabet 包含了26个大写字母
#         letters = "".join(letters)
#         if letters == "GOV":
#             continue
#         for numbers in range(1000):
#             yield f"{letters} {numbers:03}"


# # yield 语句令该函数成为生成器，当程序执行到该处，值被返回
# # 接着生成器等待对 __next__() 的另一次调用
# # 然后生成器会从之前停止的地方重新开始，生成下一个值

# # 必须调用生成器函数才能创建想要使用的生成器迭代器
# # 将生成器迭代器绑定到名称 license_plates
# # 现在它是一个具有 __next__()方法的对象
# # 利用 license_plates 遍历所有可能的车牌号
# license_plates = gen_license_plates()
# for plate in license_plates:
#     print(plate)  # AAA000 ~ ZZZ999

# # 有条件地使用生成器，为申请者登记新的车牌号
# registrations = {}

# def new_registration(owner):
#     if owner not in registrations:
#         # 如果字典中没有该车主 owner
#         plate = next(license_plates)
#         # 生成车牌号 plate
#         registrations[owner] = plate
#         # 并登记到字典
#         return plate
#     return None

# # 快速跳过一些车牌
# for _ in range(4441888):
#     next(license_plates)
# name = "Jason C. McDonald"
# my_plate = new_registration(name)
# print(my_plate)  # GOE 888
# print(registrations[name])  # GOE 888

# # 生成器 vs 迭代器类
# # 迭代器类中的 __next()__ 方法能引发 StopIteration 异常
# # 生成器不需要、甚至不允许（3.5版本后）显式引发异常
# # 当生成器函数终止，无论是到达末尾还是显式地使用 return 语句
# # 都在幕后自动引发 StopIteration 异常

# # 作为迭代器类

# from random import choice
# colors = ["red", "green", "blue", "silver", "white", "black"]
# vehicles = ["car", "truck", "semi", "motorcycle", None]
# class Traffic:
#     # 没有实例属性，所以不需要初始化器
#     # 定义特殊方法 iter 使类变成可迭代的
#     def __iter__(self):
#         return self
#     # 随机选择车和颜色，组合成格式化字符串
#     def __next__(self):
#         vehicle = choice(vehicles)
#         # 如果车子随机到 None，停止迭代
#         if vehicle is None:
#             raise StopIteration
#         color = choice(colors)
#         return f"{color} {vehicle}"

# count=0
# for count, vehicle in enumerate(Traffic(), start=1):
#     print(f"Wait for {vehicle}...")
# print(f"Merged after {count} vehicles!")

# # 作为生成器函数
# from random import choice
# colors = ["red", "green", "blue", "silver", "white", "black"]
# vehicles = ["car", "truck", "semi", "motorcycle", None]
# def traffic():
#     while True:
#         vehicle=choice(vehicles)
#         if vehicle is None:
#             return
#             # 通过 return 退出，并在幕后引发 StopIteration
#             # 直接引发 StopIteration 会促发 RuntimeError
#         color=choice(colors)
#         yield f"{color} {vehicle}"
# count=0
# for count, vehicle in enumerate(traffic(), start=1):
#     print(f"Wait for {vehicle}...")
# print(f"Merged after {count} vehicles!")

# 生成器关闭
# 
#
#
#
#
#
#
#
#

# --------------------------------------------------------------------------------------------
# # # yield from

#


# --------------------------------------------------------------------------------------------
# # # 生成器表达式

#


# --------------------------------------------------------------------------------------------
# # # 列表推导式

#


# --------------------------------------------------------------------------------------------
# # # 集合推导式

#


# --------------------------------------------------------------------------------------------
# # # 字典推导式

#


# --------------------------------------------------------------------------------------------
# # # 生成器表达式的隐患

#


# --------------------------------------------------------------------------------------------
# # # 简单协程

#


# --------------------------------------------------------------------------------------------
# # # 异步又如何？

#


# --------------------------------------------------------------------------------------------
# # # 本章小结

#
