# # # # 容器与迭代 # # # #

# 遍历数组是程序中最基本的算法之一
# 然而在python中，循环和容器在完全不同的层次上运行

# 注：collection 翻译作容器，set 翻译作集合，以示区分
# 故此将章节名称从 set 改为 collection


# --------------------------------------------------------------------------------------------
# # # 循环

# # while 循环
# # 传统的循环，只要标头中的表达式的计算结果为True，循环体就会执行
# # 案例：输入数字

# number = None
# while number is None:
#     try:
#         number = int(input("Enter a number:"))
#     except ValueError:
#         print("You must enter a number")
# print(f"You entered {number}")
# # 一旦用户输入一个有效的整数，就会退出循环

# # 选择退出机制：break 关键字
# number = None
# while number is None:
#     try:
#         raw = input("Enter a number ('q' to quit): ")
#         if raw == "q":
#             break
#         number = int(raw)
#     except ValueError:
#         print("You must enter a number")
#     else:
#         print(f"You entered {number}")

# # for 循环
# # 遍历或迭代一组值，也可以有 else 子句
# # 案例：打印列表

# numbers = ["one", "two", "three"]
# for number in numbers:
#     print(number)
# else:
#     print("We're done!")

# --------------------------------------------------------------------------------------------
# # # 集合

# # 一种容器，包含以某种方式组织的 n 项，每一项都被绑定到一个值，
# # 注意，值本身不包含在集合中！
# # 集合包括元组、列表、双端队列、可变集合和字典，每种集合都有多种变体

# # 在 python 交互式 shell 中查阅内建文档来了解更多详情
# # 在终端 terminal 中输入命令行 python 进入交互式 shell ，此时提示符变成 >>>
# # 输入 help(list)、help(str)、help(len) 可查看具体词条内容
# # 按 space 翻页，按 q 退出分页，输入 quit() 可退出交互式 shell

# # 元组 tuple
# # 不可变序列，即，不能添加、删除、排序元素
# # 通常用于存储异构类型的顺序排列的数据
# order = ("Jason", "pumpkin spice latte", 12)
# # 用逗号分隔值序列，并用方括号括起来

# # 通过方括号中指定的索引来访问元素
# print(order[1])
# [1] 表示第二个元素

# # 只包含一个元素的元组，在元素后保留逗号
# orders = ("pumpkin spice latte",)
# # 当预期返回一个不确定多少元素的元组时就能这么做

# # 具名元组 named tuple
# # collections 模块中提供的元组变体
# # 主要用途是给值添加键

# from collections import namedtuple
# 先定义键/字段名
# CoffeeOrder = namedtuple("CoffeeOrder", ("item", "addons", "to_go"))
# 再绑定值
# order = CoffeeOrder("pumpkin spice latte", ("whipped cream",), True)
# print(order.item)
# print(order[2])
# # 能通过字段名或下标索引来访问 order 中的值
# # 大多数时候可以用 字典 或 类 实现相似的功能

# # 列表 list
# # 可变的序列集合，即，可以添加、删除、排序元素
# # 通常用于存储同类型的顺序排列的数据
# specials = ["pumpkin spice latte", "caramel macchiato", "mocha cappuccino"]
# print(specials[1])
# # 仍用逗号分隔值序列，用圆括号括起来
# # 可将列表用作数组、堆栈或队列

# # 用 pop() 删除元素，用 append() 增加元素，用 insert() 在特定位置增加元素
# drink = specials.pop()
# print(drink)
# print(specials)
# drink = specials.pop(1)
# print(drink)
# print(specials)
# specials.append("cold brew")
# print(specials)
# specials.insert(1, "americano")
# print(specials)

# # 双端队列 deque /dek/
# # collections 模块提供的列表变体
# # 针对首末两个元素的操作进行了优化，在意性能时，它特别是和用作堆栈或队列

# # 可以用 popleft() 和 appendleft() 从头删除、增加元素
# from collections import deque
# customers = deque(['Daniel', 'Denis'])
# print(customers)
# customers.append('Simon')
# print(customers)
# customers.popleft()
# print(customers)
# customers.appendleft('James')
# print(customers)
# customers.pop()
# print(customers)

# # 可变集合 set
# # 可变的无序集合，所有元素 # 必须唯一 #
# # 添加重复元素的操作会被忽略，主要使用 set 进行快速检查及数学集合的相关操作
# # 尤其在大型数据集中
# # 存储在可变集合中的每个值都必须是 # 可哈希 # 的
# raffle = {"James", "Denis", "Simon"}
# # 用逗号分隔元素，用花括号括起来
# # 因为是无序的，只能通过值来索引元素
# # 用 add() 增加元素，用 discard() 或 remove() 来删除元素，
# # pop() 也能删除但无法给定参数，所以是（不完全）随机的
# print(raffle)
# raffle.add("Daniel")
# print(raffle)
# raffle.add("Denis")
# print(raffle)
# raffle.discard("Simon")
# print(raffle)
# raffle.discard("Neil")  # 不会引发 KeyError
# print(raffle)
# # raffle.remove('Neil')  # 会引发 KeyError
# raffle.pop()  # 总是会删掉集合中的第一项（但你无法确定是谁）
# print(raffle)
# # 空集合用 set() 表示，{} 代表空白字典

# 不可变集合 frozenset
# 不可变的无序集合，所有元素唯一

# # 案例：储存往期获奖人员名单
# raffle = {"Kyle", "Denis", "Jason"}
# prev_winners = frozenset({"Denis", "Simon"})

# # 可变、不可变集合支持数学和逻辑运算符
#     # 并集      |
#     # 交集      &
#     # 差集      -
#     # 对称差集  ^
#     # 子集      <或<=
#     # 超集      >或>=

# raffle -= prev_winners
# print(raffle)
# winner = raffle.pop()
# print(winner)

# # 字典 dict
# # 以键值对的形式存储数据的可变集合，体现键值对间的映射关系
# # 键可以是任何可哈希的类型，值可以是任何值
# # 其它编程语言中，这种类型的数据称为哈希表，无论数据量大小，查找总是很快
# menu = {"drip": 1.95, "cappuccino": 2.95}
# # 键与值用冒号分隔，键值对间用逗号分隔，再用花括号把它们括起来
# # 通过在方括号中指定键来访问各个元素，访问的键不在字典中，则引发 KeyError
# print(menu["drip"])
# # 也可以赋值或修改元素
# menu["americano"]=2.49
# print(menu)
# # 用 del 关键字删除键值对
# del menu["americano"]
# print(menu)

# # 检查还是异常
# # 为了规避 KeyError 可以选择 EAFP 或 LBYL 策略

# # EAFP 策略
# menu = {"drip": 1.95, "cappuccino": 2.95, "americano": 2.49}

# def checkout(order):
#     try:
#         print(f"Your total is {menu[order]}.")
#     except KeyError:
#         print("That item is not on the menu.")
# checkout("drip")
# checkout("tea")
# # ？这种方法更适用于无效键处于异常情况的场景
# # 通常，except 子句在性能方面的开销，更加昂贵，但是是合理的

# # LBYL 策略
# menu = {"drip": 1.95, "cappuccino": 2.95, "americano": 2.49}

# def checkout(order):
#     if order in menu:
#         print(f"Your total is {menu[order]}.")
#     else:
#         print("That item is not on the menu.")
# checkout("drip")
# checkout("tea")
# # 希望经常检查键是否有效，这种方法更可取
# # 失败比例外更常见，以上两种策略在理想情况下具有大致相同的性能
# # 当无效键处于一种特殊情况时，LBYL 策略通常就不受欢迎了，因为要查找有效键两次：
# # 检查时和使用时
# # 相比之下，EAFP 策略只需访问一次有效键，因为它能处理可能引发的 KeyError

# # 字典变体
# # 在 collections 模块中提供了内置字典的变体
# # DefaultDict允许指定生成默认值的可调用对象
# # OrderDict 具有跟踪、管理键值对顺序的额外功能
# # Counter 专为计算可哈希对象而设计的，对象是键，计数为整数值
#     # 其它变成语言中被称为多重集合（multiset）


# --------------------------------------------------------------------------------------------
# # # 容器的解包

# # 所有容器都可以解包到多个变量中，即，每个元素都有自己的名称

# from collections import deque
# customers = deque(["Kyle", "Simon", "James"])
# first, second, third = customers
# print(first)
# # 解包线性容器时，等号左侧的名称外不需要使用括号
# # 解包的主要限制：必须知道要解包的值有多少个！
# customers.append("Daniel")
# first, second, third = customers  # ValueError
# first, second, third, _ = customers
# print(first)
# first, second, _, _ = customers
# print(first)
# # 可以用下划线来忽略第四个值
# baristas = ("Jason",)
# (barista,) = baristas
# print(barista)
# # 如果要解包只包含一个值的容器，在解包到的名称后保留括号

# # 星号表达式
# # 如果不知道容器中还有多少额外值，可以使用星号表达式捕获未解包的值
# from collections import deque
# customers = deque(["Kyle", "Simon", "James", "Daniel"])
# first, second, *rest = customers
# print(first)
# print(rest)

# # 可以在任何位置使用星号表达式
# first, *middle, last = customers
# print(middle)
# print(last)
# # 或者用星号表达式忽略多个值
# *_, second_to_last, last = customers
# print(second_to_last)
# # 每个解包语句中只能有一个星号表达式——因为它是贪婪的

# # 字典的解包
# menu = {"drip": 1.95, "cappuccino": 2.95, "americano": 2.49}
# # 直接解包字典，获得键序列
# a, b, c = menu
# print(a)
# # 解包.values()，获得值序列
# a, b, c = menu.values()
# print(a)
# # 解包.items()，获得键值对序列
# a, b, c = menu.items()
# print(a)
# # 或用元组的方式同时解包键和值
# (a_name, a_price), *_=menu.items()
# print(a_name)
# print(a_price)
# # 可以使用这种带括号的解包策略来解包 # 二维容器 #

# --------------------------------------------------------------------------------------------
# # # 容器的结构模式匹配

# # 在3.10版本后可对元组、列表、字典进行结构模式匹配

# # 序列模式中，元组和列表是可以互换的
# # 序列模式使用和解包相同语法，且能使用星号表达式
# order = ["venti", "no whip", "mocha latte", "for here"]
# match order:
#     case ("tall", *drink, "for here"):
#         drink = " ".join(drink)
#         print(f"Filling ceramic mug with {drink}.")
#     case ["grande", *drink, "to go"]:
#         drink = " ".join(drink)
#         print(f"Filling large paper cup with {drink}.")
#     case ["venti", *drink, "for here"]:
#         drink = " ".join(drink)
#         print(f"Filling extra large tumbler with {drink}.")
# # 序列模式是相同的（这里翻译有点别扭），无论在方/圆括号中，按顺序比较

# # 映射模式可对特定值进行匹配，包裹在花括号中
# # 案例中检查键 size 和 serve 的值，并捕获键 drink 的值
# order = {
#     "size": "venti",
#     "notes": "no whip",
#     "drink": "mocha latte",
#     "serve": "for here",
# }
# match order:
#     case {"size": "tall", "serve": "for here", "drink": drink}:
#         print(f"Filling ceramic mug with {drink}.")
#     case {"size": "grande", "serve": "to go", **rest}:
#         drink = f"{rest['notes']} {rest['drink']}"
#         print(f"Filling large paper cup with {drink}.")
#     case {"size": "venti", "serve": "for here"}:
#         drink = f"{order['notes']} {order['drink']}"
#         print(f"Filling extra large tumbler with {drink}.")
# # 特殊地，第二个 case 中用通配符捕获剩余的键
# # 以及最后一个 case 很简单地达到了类似效果


# --------------------------------------------------------------------------------------------
# # # 以索引或键访问元素

# # 有序容器是可索引的，通过方括号指定序数访问元素
# specials = ["pumpkin spice latte", "caramel macchiato", "mocha cappuccino"]
# # 这两句是等价的，可索引集合类实现了特殊方法__getitem/setitem/delitem__()
# print(specials[1])
# print(specials.__getitem__(1))
# # 用特殊方法修改列表中的元素
# specials.__setitem__(1, "drip")


# --------------------------------------------------------------------------------------------
# # # 切片符

# 允许访问元组或列表中特定的元素或元素范围
# 切片符用冒号分隔三个部分，并用方括号括起来
# [start:stop:step]，不用指定所有参数，但要注意冒号
# orders = [
#     "caramel macchiato",
#     "drip",
#     "pumpkin spice latte",
#     "drip",
#     "cappuccino",
#     "americano",
#     "mocha latte",
# ]
# # 第3~5号元素
# slice = orders[3:6]
# print(slice)
# # 4号及之后的所有元素
# slice = orders[4:]
# print(slice)
# # 2号之前的所有元素
# slice = orders[:2]
# print(slice)
# # 倒数第一个元素
# slice = orders[-1]
# print(slice)
# # 倒数第三个及之后的所有元素
# slice = orders[-3:]
# print(slice)
# # 倒数第三、第二个元素
# slice = orders[-3:-1]
# print(slice)
# # 第1、3、5……号元素
# slice = orders[1::2]
# print(slice)
# # 反转版本
# slice = orders[::-1]
# print(slice)
# # 倒数第2、4、6……个元素
# slice = orders[-2::-2]
# print(slice)
# # 第3~5个号元素（倒序）
# slice = orders[5:2:-1]
# print(slice)
# # 复制副本（浅拷贝）
# slice = orders[:]
# print(slice)

# # ？还可以初始化一个创建切片对象，以便复用相同的切片方法
# my_slice = slice(3, 5, 2)  # TypeError？？？
# print(my_slice)

# # 使用 islice()
# # 可以使用itertools.islice()对任何容器进行切片
# # 除了不支持负值参数，行为和切片符相同
# # islice(collection, start, stop, step)
# from itertools import islice
# menu={'drip': 1.95, 'cappuccino': 2.95, 'americano': 2.49}
# menu=dict(islice(menu.items(),0,3,2))
# print(menu)

# --------------------------------------------------------------------------------------------
# # # in 运算符

# # 快速检查特定值是否在指定容器中
# orders = [
#     "caramel macchiato",
#     "drip",
#     "pumpkin spice latte",
#     "drip",
#     "cappuccino",
#     "americano",
#     "mocha latte",
# ]
# if "mocha cappuccino" in orders:
#     print("open chocolate syrup bottle")
# if "drip" not in orders:
#     print("shut off percolator")

# --------------------------------------------------------------------------------------------
# # # 检验集合的长度

# customers = ["Glen", "Todd", "Newman"]
# print(len(customers))
# # 进行迭代时，使用 len() 的次数将比预期少，这改变了容器的遍历方式
# # 毕竟这样就很少需要知道集合的具体长度了

# # 测试容器是否为空也不需要用到 len()
# # 只要判断 collection == True 即可
# customers = []
# if customers:
#     print("There are customers.")
# else:
#     print("Quiet day.")
# print(bool(customers))

# # 通常只有当需要将容器长度作为数据本身的一部分时才使用 len()
# orders_per_day = [56, 41, 49, 22, 71, 43, 18]
# average_orders = sum(orders_per_day) // len(orders_per_day)
# print(average_orders)


# --------------------------------------------------------------------------------------------
# # # 迭代

# # 所有容器都能和迭代一起工作，可通过迭代直接根据需求访问元素
# # 迭代模式不仅限于集合，可采用迭代的方式生成或处理数据，关键是 # 按需 #

# # 可迭代对象
# # 任何可以逐次按需访问元素或值的对象，例如列表
# # 可迭代对象必须有一个关联的迭代器，这是由该对象的实例方法 __iter__() 返回的

# # 迭代器
# # 执行实际迭代的对象，旨在提供对正在遍历的可迭代对象中的下一项的访问准备
# # 为了成为可迭代对象，对象需要实现特殊方法 __next__()
# # 它不接受参数，仅在遍历的可迭代对象中推进到下一项并返回该值
# # 迭代器还必须实现方法 __iter__() ，此方法返回迭代器本身（self）
# # 这种约定是必须的，这样接受可迭代对象的代码也可以毫无困难地接受迭代器

# # 所有容器都是可迭代对象，每个容器至少有一个专用的、与之关联的迭代器

# # 手动使用迭代器
# # 案例：特调迭代器
# specials = ["pumpkin spice latte", "caramel macchiato", "mocha cappuccino"]
# # 获取迭代器
# first_iterator = specials.__iter__()
# second_iterator = specials.__iter__()
# print(type(first_iterator))  # <class 'list_iterator'>
# # 使用迭代器访问列表，首先访问列表的第一个元素
# item = first_iterator.__next__()
# print(item)  # pumpkin spice latte
# # 然后是第二个元素
# item = first_iterator.__next__()
# print(item)  # caramel macchiato
# # 每个迭代器会分别跟踪其在可迭代对象中的位置
# item = second_iterator.__next__()
# print(item)  # pumpkin spice latte
# # 第一个迭代器还记得自身的位置
# item = first_iterator.__next__()
# print(item)  # mocha cappuccino
# # 完成遍历后再次调用就会引发特殊异常 StopIteration
# item = first_iterator.__next__()  # raises StopIteration

# # 通常不用手动调用 __iter__() 和 __next__() 方法
# # 可使用 python 内置的函数 iter() 和 next() ，分别传入可迭代对象或迭代器
# # 特殊方法将在幕后自动被调用
# first_iterator = iter(specials)
# second_iterator = iter(specials)
# print(type(first_iterator))
# item=next(first_iterator)
# print(item)
# item=next(first_iterator)
# print(item)
# # 效果和上一段代码是一样的

# # 这种手动方法存在很多重复
# # 下面把相同的手动迭代逻辑封装在一个while循环中
# iterator = iter(specials)
# while True:
#     try:
#         item = next(iterator)
#     except StopIteration:
#         break
#     else:
#         print(item)
# # 一旦引发了 StopIteration ，说明已经遍历了所有元素，则可以跳出循环

# # 使用 for 循环是处理迭代的标准方式，这样会隐式调用 iter() 和 next()
# specials = ["pumpkin spice latte", "caramel macchiato", "mocha cappuccino"]
# for item in specials:
#     print(item)
# # 这样就不用直接获取迭代器了

# # 用 for 循环迭代
# # 对于循环和迭代来说：永远不要用 # 计数器变量 # 进行循环控制
# # 因为在 python 中，可迭代对象能直接控制 for 循环
# # 案例：客户排队列表
# customers = [
#     "Newman", "Daniel", "Simon", "James", "William", "Kyle",
#     "Jason", "Devin", "Todd", "Glen", "Denis",
# ]
# # 每次迭代中，将当前元素绑定到 customer ，使其像任何其他变量一样在循环代码块中工作
# for customer in customers:
#     pass  # do something with customer
#     print(f"Order for {customer}!")

# # 线性集合非常简单
# # 任何给定元素中具有 # 多个值 # 的迭代器，都必须区别对待
# customers = [
#     ("Newman", "tea"),
#     ("Daniel", "lemongrass tea"),
#     ("Simon", "chai latte"),
#     ("James", "medium roast drip, milk, 2 sugar substitutes"),
#     ("William", "french press"),
#     ("Kyle", "mocha cappuccino"),
#     ("Jason", "pumpkin spice latte"),
#     ("Devin", "double-shot espresso"),
#     ("Todd", "dark roast drip"),
#     ("Glen", "americano, no sugar, heavy cream"),
#     ("Denis", "cold brew"),
# ]
# for customer, drink in customers:
#     print(f"Making {drink}...")
#     print(f"Order for {customer}!")
# # 以上代码在遍历时将每个元组解包成两个名称：customer 和 drink

# # 在循环中对集合进行排序
# # 循环允许对数据进行高级处理，如排序
# # 案例：获得饮品清单（A-Z）
# for _, drink in sorted(customers, key=lambda x: x[1]):
#     print(f"{drink}")
# # 用 sorted 函数对列表 customers 进行排序（默认为升序）
# # 排序依据 key 为一个匿名函数，指定为每个元组中的第 1 项
# # 此外，我们用下划线忽略每个元组中的第 0 项，因为这个案例中用不到它们
# # 这通常是 for 循环中从元组中挑选元素的最佳方式
# # 另一方面，如果每个元素都是一个包含很多子元素的容器
# # 那么将元素整体绑定到一个名称并在循环中访问需要的内容可能会更好

# # 枚举循环
# # 永远不需要计数器！
# # 如果需要索引本身应该怎么做？enumerate() 函数
# # 它适用于所有可迭代对象，甚至包括那些不能通过下标访问的对象
# for number, (customer, drink) in enumerate(customers, start=1):
#     print(f"#{number}. {customer}: {drink}")
# # enumerate() 返回包含了计数值（有时是索引）、元素的 # 元组 #
# # 计数默认从 0 开始，但也可以通过参数 start 来调整
# # 由于本例中的元素本身是元组，因此必须使用带括号的复合解包来获得元素的元素

# # 循环中的突变
# # 案例：用 deque 记录客户队列，并在服务后删除客户
# from collections import deque

# customers = deque(
#     [
#         ("Newman", "tea"),
#         ("Daniel", "lemongrass tea"),
#         ("Simon", "chai latte"),
#         ("James", "medium roast drip, milk, 2 sugar substitutes"),
#         ("William", "french press"),
#         ("Kyle", "mocha cappuccino"),
#         ("Jason", "pumpkin spice latte"),
#         ("Devin", "double-shot espresso"),
#         ("Todd", "dark roast drip"),
#         ("Glen", "americano, no sugar, heavy cream"),
#         ("Denis", "cold brew"),
#     ]
# )
# # 以下是问题代码
# for customer, drink in customers:  # RuntimeError: deque mutated during iteration
#     print(f"Making {drink}...")
#     print(f"Order for {customer}!")
#     customers.popleft()
# # 问题是，当next(iter(customers)) 还未进入到下一个循环前我们就删除了当前元素
# # 迭代器便不知道下一个元素是谁，从而导致各种未定义行为
# # 强调！迭代的同时改变容器，不论追加、删除、排序，通常会引发 RuntimeError

# # 解法一 - 制作副本
# for customer, drink in customers.copy():
#     print(f"Making {drink}...")
#     print(f"Order for {customer}!")
#     customers.popleft()
# print(customers)
# # 注：这里不能使用冒号切片符，它不支持双端队列
# # 这里的方法不是理想的解决方案
# # ？浅拷贝不是绑定的吗，为什么不会报错？

# # 解法二 - 使用 while 循环
# while customers:
#     customer, drink = customers.popleft()
#     print(f"Making {drink}...")
#     print(f"Order for {customer}!")
# # 循环会一直迭代直至 customers 清空

# # 案例：迭代的同时扩展、重排
# # 设定：对于订购的每种咖啡，稍后都做一份相同的（将相同口味的咖啡追加到列表末尾）

# # 问题代码
# orders = ["pumpkin spice latte", "caramel macchiato", "mocha cappuccino"]
# for order in orders:
#     orders.append(order)  # creates infinite loop!

# # 解决方案 - 我们需要创建一个新集合！
# new_orders = orders[:]
# for order in orders:
#     new_orders.append(order)
# orders = new_orders
# print(orders)

# # 嵌套循环和替代方案
# # 案例：每个人喝每种咖啡
# from itertools import product
# samples = ["Costa Rica", "Kenya", "Vietnam", "Brazil"]
# guests = ["Denis", "William", "Todd", "Daniel", "Glen"]
# for sample in samples:
#     for guest in guests:
#         print(f"Give sample of {sample} coffee to {guest}.")
# # 记住：扁平好过嵌套！
# # 首先，嵌套的可读性差、易错、缩进地狱
# # 其次，跳出嵌套循环是不可能的， break 和 continue 不再好用

# # 用 itertools 模块中的 product() 函数可以在一次循环中获得嵌套循环的效果
# for sample, guest in product(samples,guests):
#     print(f"Give sample of {sample} coffee to {guest}.")
# # product() 可以将多个可迭代对象组合为一个单独的可迭代对象 - 包含所有组合的元组
# # 解包后就可以用名称分别访问每层循环组中的各个值
# # 迭代函数和 itertools 模块基本涵盖了绝大多数嵌套循环场景
# # 实在不行我们还有 # 可迭代函数 # 或 # 可迭代类 #


# --------------------------------------------------------------------------------------------
# # # 迭代工具

# # 有很多工具可用于迭代各种容器

# # ？基础内建工具
# # all() 在可迭代对象中所有项的计算结果都为 True 时，返回 True
# # any() 在可迭代对象中任意项的计算结果为 True 时，返回 True
# # enumerate() 是一个迭代器，对传递进来的迭代器内元素返回元组
# # 该元组的第一个值是元素索引，第二个值是元素本身
# # 甚至是用于不可索引的可迭代对象
# # 通过 start 参数，定义了首个索引的整数值
# # max() 和 min() 返回可迭代对象中的最大项和最小项
# # 可选参数 key 指定了排序依据
# # range(start, stop, step) 返回从 start 开始到小于 stop 的整数序列
# # reversed() 返回倒序遍历的迭代器
# # sorted() 返回排序后的列表
# # 可选参数 key 指定了排序依据
# # sum() 返回可迭代对象中所有元素的总和，要求所有元素都是数值
# # 可选参数 start 指定了求和前的初值

# # filter
# # 可迭代过滤器 filter 允许在可迭代对象中搜索符合特定条件的值
# # 案例：有多少订单需要 drip 咖啡？
# orders = [
#     "cold brew",
#     "lemongrass tea",
#     "chai latte",
#     "medium drip",
#     "french press",
#     "mocha cappuccino",
#     "pumpkin spice latte",
#     "double-shot espresso",
#     "dark roast drip",
#     "americano",
# ]
# drip_orders = list(filter(lambda s: "drip" in s, orders))
# print(f"There are {len(drip_orders)} orders for drip coffee.")
# # 初始化器 filter() 接收两个参数：执行过滤的可调用对象，和，要过滤的可迭代对象
#     # 执行过滤的可迭代对象，可以是函数、匿名函数、其它可视为函数的对象
#     # 它必须能返回 Bool 值，用于判断元素是舍弃还是保留

# # map
# # 将可迭代对象中的每个元素作为参数传递给可调用对象
# # 然后将返回值作为自己的当前迭代值回传
# # 案例：制作咖啡
# orders = [
#     "cold brew",
#     "lemongrass tea",
#     "chai latte",
#     "medium drip",
#     "french press",
#     "mocha cappuccino",
#     "pumpkin spice latte",
#     "double-shot espresso",
#     "dark roast drip",
#     "americano",
# ]
# # 定义制作咖啡的函数
# def brew(order):
#     print(f"Making {order}...")
#     return order
# # 创建了一个 map 可迭代实例，将可迭代对象 orders 中的元素作为参数传递给 brew 函数
# for order in map(brew, orders):
#     print(f"One {order} is ready!")
# # 函数的返回值接着由 map 传回循环，并被绑定到 order

# # 可以将map()和多个可迭代对象一起使用
# # 一旦一个迭代完成用完了值，映射就完成了
# # 案例：添加价格与小费4
# from operator import add
# cost = [5.95, 4.95, 5.45, 3.45, 2.95]
# tip = [0.25, 1.00, 2.00, 0.15, 0.00]
# # 将 cost 和 tip中的元素依次传递给 add 函数
# for total in map(add, cost, tip):
#     print(f'{total:.02f}')

# # zip
# # 将多个可迭代组合，迭代时依次取出每个可迭代对象的下一个值并打包成元组
# # 案例：常客们的订单
# regulars = ["William", "Devin", "Kyle", "Simon", "Newman"]
# usuals = [
#     "french press", "double-shot espresso",
#     "mocha cappuccino", "chai latte", "tea", "drip",
# ]
# usual_orders = dict(zip(regulars, usuals))
# print(usual_orders.items())

# itertools
# 该模块包含很多用于处理迭代的类，在需要的时候请勤加查看官网或文档
# 重要的函数（跳过大部分可选参数）
# accumulate(): 重复双参数函数，调用结果作为下一次调用的第一参数，当前项作为第二参数
# chain(): 生成列表，按顺序依次传递每个可迭代对象中的每个元素
# combinations(): 根据可迭代对象生成所有可能元素的所有 n 元组合
# dropwhile(): 检验表达式，依序抛弃值为 True 的元素，返回第一个 False 和之后的所有元素
# filterfalse(): 原理同 filter()
# islice(): 对不可索引的可迭代对象执行切片，不支持负值参数
# permutations(): 根据可迭代对象生成所有可能元素的所有 n 元排列
# product(): 根据所提供对象生成笛卡尔积
# starmap(): 类似 map ，只是将提供的迭代器中的元素作为加星号的参数传递
# takewhile(): 和 dropwhile() 完全相反，返回第一个 False 之前的所有元素


# --------------------------------------------------------------------------------------------
# # # 自定义可迭代类

# # 需要编写两个类：可迭代对象、相应的迭代器
# # 前者负责存储或生成值，后者负责追踪可迭代对象中的当前位置
# # 这样可以为同一个可迭代对象创建多个独立的迭代器

# # 案例：订单系统
# class CafeQueue:
#     # 可迭代类
#     def __init__(self):
#         self._queue = []  # 包含客户姓名
#         self._orders = {}  # 存储客户订单
#         self._togo = {}  # 存储客户希望堂食/外带

#     def __iter__(self):
#         # 为了使类可迭代，必须定义特殊方法 __iter__()，方法返回迭代器的实例
#         return CafeQueueIterator(self)

#     def add_customer(self, customer, *orders, to_go=True):
#         # 实例方法：添加客户
#         self._queue.append(customer)
#         self._orders[customer] = tuple(orders)
#         self._togo[customer] = to_go

#     def __len__(self):
#         # 特殊方法，用来检查队列中的客户人数
#         # 注意，不要在循环头中直接使用len()作为迭代的一部分
#         return len(self._queue)

#     def __contains__(self, customer):
#         # 特殊方法，判断队列中是否存在指定客户对应的订单
#         return customer in self._queue


# class CafeQueueIterator:
#     # 迭代器，只接受一个参数：和迭代器实例关联的可迭代实例
#     def __init__(self, cafe_queue: CafeQueue):
#         self._cafe = cafe_queue  # 订单队列，提供详细数据
#         self._position = 0  # 当前位置，负责跟踪

#     def __next__(self):
#         # 特殊方法，负责跟踪迭代器在可迭代对象中的位置
#         # 迭代可以是无限的，没后内置的停止迭代的方法
#         # 除非出现异常 StopIteration 否则最终更新迭代器位置
#         # 并返回当前元素的相关数据
#         try:
#             customer = self._cafe._queue[self._position]
#         except IndexError:
#             raise StopIteration
#         orders = self._cafe._orders[customer]
#         togo = self._cafe._togo[customer]
#         self._position += 1  # 备注：init 中未初始化 = 0，导致 _position 无法自动补全
#         return (customer, orders, togo)  # 将数据打包为元组，方便在 for 循环中解包

#     def __iter__(self):
#         # 特殊方法，总是返回实例自身
#         return self


# # 声明 CafeQueue 类实例 queue ，向其中添加客户
# queue = CafeQueue()
# queue.add_customer("Newman", "tea", "tea", "tea", "tea", to_go=False)
# queue.add_customer("James", "medium roast drip, milk, 2 sugar substitutes")
# queue.add_customer("Glen", "americano, no sugar, heavy cream")
# queue.add_customer("Jason", "pumpkin spice latte", to_go=False)
# # 测试添加情况
# print(len(queue))
# print("Glen" in queue)
# print("Kyle" in queue)


# # 声明函数 brew 来处理订单 CafeQueue._orders[customer]（它们是长度未知的元组）
# # 这是一个简洁的版本
# def brew(order):
#     print(f"(Making {order}...)")
#     return order

# # 遍历、解包、嵌套循环、输出结果
# for customer, orders, to_go in queue:
#     for order in orders:
#         brew(order)
#     if to_go:
#         print(f"Order for {customer}!")
#     else:
#         print(f"Takes order to {customer}!")

# # python 中的 for 循环是专门为处理可迭代对象和迭代器而设计的
