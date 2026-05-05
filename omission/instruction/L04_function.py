# # # # 函数和匿名函数

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

# --------------------------------------------------------------------------------------------
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

# --------------------------------------------------------------------------------------------
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

# --------------------------------------------------------------------------------------------
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

# --------------------------------------------------------------------------------------------
# # # 关键字参数

# # 位置参数：按照输入的顺序映射的参数
# # 关键字参数：通过将标签附加到函数调用中的实参上，解决可读性问题
# dice_cup = roll_dice(6, 5)
# dice_cup = roll_dice(sides=6, dice=5)
# # 不必按顺序列出
# dice_cup = roll_dice(dice=5, sides=6)
# # 简化了函数调用，甚至可以混合使用位置参数和关键字参数
# import random
# def roll_dice(sides=6, dice=1):
#     return tuple(random.randint(1, sides) for _ in range(dice))
# dice_cups = roll_dice(dice=5)
# print(dice_cups)
# dice_cups = roll_dice(6, dice=5)
# print(dice_cups)

# --------------------------------------------------------------------------------------------
# # # 重载函数

# # 重载函数：具有相同名称但参数不同的多个函数
# # 支持重载函数的编程语言都提供了一致的接口(函数名称)，支持不同类型的参数
# # 通过动态类型、鸭子类型、可选参数，python可以编写一个函数处理所有场景
# # python不需要重载函数
# # 如果一定需要，可使用单分派泛型函数(single dispatch generic function)来创建

# --------------------------------------------------------------------------------------------
# # # 可变参数

# # 有时我们不知道需要多少个参数，这可以用任意参数列表解决
# # 这需要在参数名称前加一个星号(*)
# # 譬如掷骰子，我希望掷出多个骰子，每个骰子面数可能不同
# import random
# def roll_dice(*dice):
#     return tuple(random.randint(1,d) for d in dice)
# dice_cup=roll_dice(6,6,6,6,6)
# print(dice_cup)
# dice_cup=roll_dice(20,6,8,4)
# print(dice_cup)
# # 传递给函数的所有参数都被打包到一个元组中，绑定到名称dice
# # 可变参数必须位于函数定义中的任何位置参数之后
# # 可变参数之后的任何参数都只能用作关键字参数

# # 递归版本
# import random
# def roll_dice(*dice):
#     if dice:
#         roll = random.randint(1, dice[0])
#         return (roll,) + roll_dice(*dice[1:])
#     return ()
# dice_cup = roll_dice(3, 4, 5, 6, 7)
# print(dice_cup)
# # 递归调用函数时，使用列表切片[1:]来删除第一项

# --------------------------------------------------------------------------------------------
# # # 关键字可变参数

# # 为捕获位置数量的关键字参数，在参数名称前加两个星号(**)
# # 当需要将参数#盲目地#传递给另一个函数调用时，关键字可变参数就很有用
# def call_something_else(func, *args, **kwargs):
#     return func(*args, **kwargs)
# def say_hi(name):
#     print(f"Hello, {name}!")
# call_something_else(say_hi, name="Bob")
# # func是位置参数，args是可变参数，kwargs是关键字可变参数
# # 后两个可变参数都可以为空，不影响正常工作

# --------------------------------------------------------------------------------------------
# # # 仅关键字参数、仅位置参数

# # 可使用可变参数将一些关键字参数转换为仅关键字参数
# import random
# def roll_dice(*, sides=6, dice=1):
#     return tuple(random.randint(1, sides) for _ in range(dice))
# dice_cup = roll_dice(sides=6, dice=5)
# print(dice_cup)
# # 使用位置参数则会抛出异常TypeError

# # 当参数名称不明确、未来可能更改时，可使用仅位置参数
# # 仅位置参数在参数列表中，放在(,/)之前
# import random
# def roll_dice(dice=1, /, sides=6):
#     return tuple(random.randint(1, sides) for _ in range(dice))
# dice_cup = roll_dice(4, 20)
# print(dice_cup)
# dice_cup = roll_dice(4)
# print(dice_cup)
# dice_cup = roll_dice(sides=20)
# print(dice_cup)
# dice_cup = roll_dice(dice=4)  # TypeError
# print(dice_cup)
# dice_cup = roll_dice(dice=4, sides=20)  # TypeError
# print(dice_cup)

# # 小结
# def func(pos_only=None,/,pos_kw=None,*,kw_only=None):
#     pass

# --------------------------------------------------------------------------------------------
# # # 嵌套函数

# # 想在函数中复用一些逻辑，但不想创建另一个函数，可以在函数中嵌套函数
# # 使用嵌套函数改进roll_dice()的递归版本
# import random
# def roll_dice(sides=6, dice=1):
#     def roll():
#         return random.randint(1, sides)
#     if dice < 1:
#         return ()
#     return (roll(),) + roll_dice(sides, dice - 1)
# dice_cup=roll_dice(sides=6,dice=5)
# print(dice_cup)
# # 嵌套函数可以访问其#封闭作用域#的名称
# # ?如果想在嵌套函数内部重新绑定或改变其中任何名称，则须使用nonlocal关键字

# --------------------------------------------------------------------------------------------
# # # 闭包

# # 可以创建一个函数，用它构建并返回一种称为闭包的对象，闭包包含一个或多个nonlocal名称
# # 这样能生成闭包的函数，其实就是一个函数工厂
# import random
# def make_dice_cup(sides=6, dice=1):
#     def roll():
#         return tuple(random.randint(1, sides) for _ in range(dice))
#     return roll
# roll_for_damage = make_dice_cup(sides=8, dice=5)
# damage = roll_for_damage()
# print(damage)
# # 外部函数make_dice_cup()有两个参数，嵌套函数roll()也使用量相同的参数
# # 外部函数返回该嵌套函数时(没有括号!!!)，它变成了一个闭包
# # 将make_dice_cup()返回的闭包绑定到名称roll_for_damage上
# # roll_for_damage继续使用之前指定的sides和dice
# # 可将其作为一个函数来调用，而不需要任何参数
# # 注意：可能违反函数式编程的规则！！！
# # 如果闭包有能力改变它所封闭的值，就变成了事实上的对象，且难以调试

# # 错误使用闭包实现递归的例子
# import random
# def make_dice_cup(sides=6, dice=1):
#     def roll():
#         nonlocal dice
#         if dice < 1:
#             return ()
#         die = random.randint(1, sides)
#         dice -= 1
#         return (die,) + roll()
#     return roll
# roll_for_damage = make_dice_cup(sides=8, dice=5)
# damage = roll_for_damage()
# print(damage)
# damage = roll_for_damage()
# print(damage)  # print: "()"
# # 第一次使用闭包roll_for_damage()时一切正常，但退出函数时dice没有被重置
# # 因此在之后的调用中dice的值都为0

# # 修正如下
# import random
# def make_dice_cup(sides=6, dice=1):
#     def roll(dice=dice):
#         if dice < 1:
#             return ()
#         die = random.randint(1, sides)
#         return (die,) + roll(dice-1)
#     return roll
# roll_for_damage = make_dice_cup(sides=8, dice=5)
# damage = roll_for_damage()
# print(damage)
# damage = roll_for_damage()
# print(damage)  # print: "()"
# # 这个版本使用nonlocal名称dice作为新的局部参数dice的默认值
# # 它仍然封闭了sides和dice，但不重新绑定它们

# # 有状态闭包
# # 很少时候，有必要创建有状态闭包——在调用之间保留一些状态以供使用的闭包
# import random
# def start_turn(limit,dice=5,sides=6):
#     def roll():
#         nonlocal limit
#         if limit<1:
#             return None
#         limit-=1
#         return tuple(random.randint(1,sides) for _ in range(dice))
#     return roll
# turn1=start_turn(limit=3)
# while toss:=turn1():
#     print(toss)
# turn2=start_turn(limit=3)
# while toss:=turn2():
#     print(toss)
# # 闭包roll()只允许调用者最多重新掷骰子limit次，达到限制次数后返回None
# # 并创建一个新的闭包
# # 有状态闭包在编写整个类会带来太多样板代码的情况下可能很有用
# # 由于只有一个状态变量limit，而且使用方式可预测，此种方法是可接受的
# # 更复杂的情况下，调试将变得很困难
# # 每当在闭包中看到nonlocal时都要非常小心，它表明存在#状态#
# # 使用有状态闭包不是进行纯函数式编程！

# --------------------------------------------------------------------------------------------
# # # lambda表达式

# # 是由表达式组成的匿名函数
# # lambda x, y: x + y
# # 冒号左侧是参数列表，可省略
# # 冒号右侧是return表达式，匿名函数会求值并隐式返回结果
# # 使用lambda表达式，必须将其绑定到名称(赋值或作为另一个函数的参数)
# add = lambda x, y: x + y  # Do not assign a `lambda` expression, use a `def`RuffE731
# answer = add(20, 22)
# print(answer)

# # lambda表达式的作用
# # 以下代码用全局名称health和xp来跟踪角色状态
# import random
# health = 10
# xp = 10
# # attempt()使用outcome来决定玩家动作action的成败(???)
# # attempt()通过比较随机数roll和参数min_roll来决定玩家动作action的成败result
# # 并调用函数outcome?，接收result参数，返回元组score
# # 并据此修改health和xp
# def attempt(action, min_roll, outcome):
#     global health, xp
#     roll = random.randint(1, 20)
#     if roll >= min_roll:
#         print(f"{action} SUCCEEDED.")
#         result = True
#     else:
#         print(f"{action} FAILED.")
#         result = False
#     scores = outcome(result)
#     health = health + scores[0]
#     print(f"Health is now {health}.")
#     xp = xp + scores[1]
#     print(f"Experience is now {xp}.")
#     return result
# # 必须为每个动作编写具体的outcome函数
# # 因此这段代码将迅速增长，难以维护
# def eat_bread(success):
#     if success:
#         return (1, 0)
#     return (-1, 0)
# def fight_ice_weasel(success):
#     if success:
#         return (0, 10)
#     return (-10, 10)
# # 尝试一个动作，传递该动作的名称、成功所需最小点数、确定结果的函数
# # 传递函数时不要包括尾随的括号，我们要传递的是函数，不是函数返回的值
# attempt("Eating bread", 5, eat_bread)
# attempt("Fighting ice weasel", 15, fight_ice_weasel)

# # 如果使用lambda表达式，可作如下修改
# attempt("Eating bread", 5, lambda success: (1, 0) if success else (-1, 0))
# attempt("Fighting ice weasel", 15, lambda success: (0, 10) if success else (-10, 10))
# 可以用一行代码创建出许多不同可能的结果
# lambda表达式只能有一个return表达式
# 因此使用短小清晰的逻辑片段，尤其当通过将逻辑保持在另一个函数调用中的用例附近来使代码更具可读性时

# # 将lambda表达式作为排序键
# # 排序键是一个可调用函数，返回应该用于排序的集合或对象的一部分，常被传递给另一个函数
# people=[
#     ("Jason","McDonald"),
#     ("Denis","Pobedrya"),
#     ("Daniel","Foerster"),
#     ("Jaime","López"),
#     ("James","Beecham")]
# by_last_name=sorted(people,key=lambda x: x[1])
# print(by_last_name)
# # key参数总是一个函数或其他可调用的对象，可通过将每一项 x=("Jason","McDonald") 传递给它，
# # 后使用该可调用对象返回的值 x[1]="McDonald" 来确定排列顺序
# # 最后得到的列表by_last_name是一个姓氏排序的结果

# --------------------------------------------------------------------------------------------
# # # 装饰器

# # 允许将函数封装在额外的逻辑层中来修改函数，而无需重写函数本身
# # 以文本冒险游戏为例
# import random
# character = "Sir Bob"
# health = 15
# xp = 0
# def eat_food(food):
#     global health
#     if health <= 0:  # 检查健康状况
#         print(f"{character} is too weak.")
#         return
#     print(f"{character} ate {food}.")
#     health += 1
#     print(f"Health: {health}  |  XP: {xp}")  # 显示当前状态
# def fight_monster(monster, strength):
#     global health, xp
#     if health <= 0:  # 检查健康状况
#         print(f"{character} is too weak.")
#         return
#     if random.randint(1, 20) >= strength:
#         print(f"{character} defeated {monster}.")
#         xp += 10
#     else:
#         print(f"{character} flees from {monster}.")
#         health -= 10
#         xp += 5
#     print(f"Health: {health}  |  XP: {xp}")  # 显示当前状态
# # 每个函数代表玩家的动作，函数间共享一些代码
# # 首先，函数检查角色健康状况
# # 其次，如果角色状况良好，改变统计数据
# # 最后，显示当前状态
# eat_food("bread")
# fight_monster("Imp", 15)
# fight_monster("Direwolf", 15)
# fight_monster("Minotaur", 19)
# # 以上的重复代码不太pythonic

# # 可以将公共代码移到一个单独函数中，但我们仍需记住在动作函数中调用它们
# # 此外，仍需要条件语句，确保角色健康状况太差时不运行代码
# # 如果想在每个函数的前后运行相同代码，可使用装饰器
# import functools
# import random
# character = "Sir Bob"
# health = 15
# xp = 0
# def character_action(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         if health <= 0:
#             print(f"{character} is too weak.")
#             return
#         result = func(*args, **kwargs)
#         print(f"Health: {health}  |  XP: {xp}")
#         return result
#     return wrapper
# # 装饰器最常见的实现方式是作为闭包（或任何可调用对象/包括类）来实现
#     # 闭包中包含对已修改函数（或任何其他可调用对象）的引用
# # 装饰器 character_action()接收func参数，这是已修改的可调用对象
#     # 装饰器内部是wrapper，是包含装饰器逻辑的可调用对象
#     # 由于不知道应用装饰器的函数将接收多少个参数，因此将wrapper设置为接收可变参数
# # @functools.wraps(func)可以防止被封装的可调用对象的身份被程序的其他部分隐藏
#     # 没有这行，封装可调用对象就会破坏对__doc__和__name__等重要函数属性的外部访问
#     # 这行本身是装饰器，确保封装的函数中保留了可调用对象的所有重要属性
#     # 从而使它们能够以所有常见的方式在函数外部访问
# # 在wrapper中放置想在每个函数前后运行的所有逻辑
#     # 首先，检查健康状况
#     # 其次，调用绑定到func的函数，并将所有可变参数解包到调用中，并将返回值绑定到result
#     # 最后，输出统计数据，并返回result
#     # 与任何闭包一样，外部函数返回内部函数

# # 然后我们使用装饰器并重构其它函数
# @character_action
# def eat_food(food):
#     global health
#     print(f"{character} ate {food}.")
#     health += 1
# @character_action
# def fight_monster(monster, strength):
#     global health, xp
#     if random.randint(1, 20) >= strength:
#         print(f"{character} defeated {monster}.")
#         xp += 10
#     else:
#         print(f"{character} flees from {monster}.")
#         health -= 10
#         xp += 5
# # 为了将装饰器应用于函数，在函数定义中列出想要应用的每个装饰器
# # 每行一个装饰器，名称前有一"@"符号
# # 装饰器按顺序应用，每个装饰器封装其下方紧邻的内容
# eat_food("bread")
# fight_monster("Imp", 15)
# fight_monster("Direwolf", 15)
# fight_monster("Minotaur", 19)
# # 应用装饰器，代码变得清晰、易于维护，新代码效果和之前一样

# --------------------------------------------------------------------------------------------
# # # 类型提示及函数注解

# # 类型提示：关于应该传入或返回什么数据类型的提示
# # 类型提示有助于文档编写
# # 类型提示能帮助更早发现潜在错误，静态类型检查器是这方面的主要工具
# # 注意！类型提示不代表将动态类型转换为静态类型
# # 注意！python会忽略这些提示，不会在错误传递时报错、尝试转换
# # 类型提示通过注解指定，注解是额外信息，解释器不处理注解
# # 变量注解：指定名称#期望#的类型
# answer: int = 42
# # 函数注解：指定参数和函数返回值的类型提示
# import typing
# def roll_dice(sides: int = 6, dice: int = 1) -> typing.Tuple[int, ...]:
#     pass
# # 如果参数默认值为None，而非期望类型的默认值，则使用类型提示typing.Optional[int]
# # 其中期望的类型int出现在括号中
# # typing.Tuple[int,...]这个元组中的每个值都应该是正数，"..."表示不确定返回多少个值
# # 如果不确定元组返回什么类型或多少类型，可用注解typing.Tuple[typing.Any,...]

# # 可以通过定义类型别名来缩短类型提示
# TupleInts = typing.Tuple[int, ...]
# def roll_dice(sides: int = 6, dice: int = 1) -> TupleInts:
#     pass
# # 用静态类型检查器运行代码，如果类型提示与实际使用不匹配，检查器会列出这些内容

# # 鸭子类型和类型提示
# # 类型提示与鸭子类型看上去不兼容，但通常可以很好配合
# # 假设一个函数可接收任意类型的参数，这些类型可迭代
# import typing
# def search(within: typing.Iterable[typing.Any]):
#     pass
# # typing.Iterable[typing.Any]表示参数within是一个可迭代对象
# # 防空壕中的.Any表示其可包含任何数据类型的元素
# # typing模块包含许多不同类型，
# # EP 484和PEP 3109分别定义了类型提示和函数注解

# # 应该使用类型提示吗
# # 用：减少由于缺乏静态类型可能产生的错误
# # 不用：使代码变得混乱，影响python通过动态类型获得的自然可读性
