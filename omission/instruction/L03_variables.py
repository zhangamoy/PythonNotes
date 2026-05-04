#
# # # 名称和值 name & value
# 1
# # python用name和value代替variable
# # 一个name指向一个value或object
# # 可以有多个name指向同一个value

# # # 赋值 assignment

# # 赋值：spam被绑定到内存中的值123456789上
# spam = 123456789
# # maps被绑定到同一块内存
# maps = spam
# # 并没有在内存中创造123456789的#副本#
# # is运算符可以检查两个名称是否被绑定到内存中的同一个值
# print(spam == maps)
# print(spam is maps)
# # 遗憾的是，spam和eggs虽然值相等，但却不一定共享同一个#身份#
# eggs = 123456789
# print(spam == eggs)
# print(spam is eggs)  # probably False
# # 在是否复用一个已经存在的值这件事上，python是比较任性的
# # 警告：is运算符检查身份，一般只建议用来检查某个东西是不是None，用==绝大多数情况更保险
# # 内置函数id()返回一个整数，表示某个名称的内存身份，这就是is本质在比较的值

# # # 数据类型

# # python是一种动态类型语言，不需要变量声明关键字
# # python还是强类型语言
# # 强调：名称有作用域，没有类型；值有类型，但没有作用域
# # 用内置函数type()可以知道某个值的数据类型——或者说值是哪个类的#实例#
# answer = 42
# print(type(answer))
# if type(answer) is int:
#     print("What's the question?")
# # 实际检查类型时，推荐使用isinstance()而不是type()，前者考虑了子类和继承
# if isinstance(answer, int):
#     print("What's the question?")
# # 鸭子类型：python不关心值的数据类型是什么，更关心值的数据类型的功能

# # # 作用域和垃圾回收

# # 名称具有作用域，可以是全局的，可以是局部的
# # 函数和推导式是python中#仅有#的定义了作用域的结构
# # 模块和类没有自己的作用域，他们只有自己的命名空间
# # 对于任何特定的(内存)值，python会保留一个引用计数
# # 值绑定到名称时，创建一个引用，当没有引用时，该值被删除
# # 这就是引用计数垃圾回收器
# # 尝试在定义message的spam()函数的上下文外访问message会引发NameError
# # 一旦退出函数，
# # 名称：message/word/separator都会被删除
# # 值：word/separator的值(由于引用计数归零)也会被删除
# # 值：message则不会被删除，因为return语句的存在
# def spam():
#     message = "Spam"
#     word = "spam"
#     # 循环没有自己的作用域
#     for _ in range(100):
#         separator = ", "
#         message += separator + word
#     message += separator
#     message += "spam!"
#     return message
# # print(message)  # undefined name
# print(output := spam())
# # 函数的#返回值#仍然存在于内存中，并能绑定到函数外的新名称output上
# # 当python程序终止时，进入解释器关闭阶段
# # 解释器讲释放所有分配的资源

# # 全局作用域
# # 当模块内的名称不在任何函数、类、列表推导式中定义时，拥有全局作用域
# # 请谨慎使用，容易导致代码难以调试和维护
# # 错误：在赋值之前使用了局部变量 high_score
# # local variable 'high_score' referenced before assignment
# high_score = 10
# def score():
#     # global high_score  # 正确做法
#     new_score = 465
#     if new_score > high_score:  # 在赋值前使用局部变量 high_score
#         print("New high score.")
#         high_score = new_score  # 给同名局部变量 high_score 赋值
# score()
# print(high_score)
# # 正确做法，使用 global 关键字声明使用全局名称 high_score

# # 类似的，下面这段代码#不会报错#，但无法实现预期效果
# current_socre = 0
# def score():
#     new_score = 465
#     current_socre = new_score
# score()
# print(current_socre)  # prints 0

# # python允许在函数中实现另一个函数
# spam=True
# def order():
#     eggs=12
#     def cook():
#         nonlocal eggs
#         if spam:
#             print("Spam!")
#         if eggs:
#             eggs-=1
#             print("...and eggs.")
#     cook()
# order()
# # 函数内只是访问全局名称 spam 并不需要做额外的事情
# # 但重新赋值则会定义新名称，并在函数内覆盖全局名称
# # nonlocal 关键字允许内部函数使用定义在外部函数中的名称
# # 这称为嵌套作用域或封闭作用域
# # 所以若没有 nonlocal ，在 cook() 内给 eggs 赋值并在赋值前使用，就会报错

# # 作用域解析顺序 LEGB
#     # Local: 局部作用域
#     # Enclosing-function locals: 外部函数的局部作用域
#     # Global: 全局作用域
#     # Built-in: 内置作用域
# # 当使用 Global 或 Nonlocal 关键字时，改变了作用域解析顺序

# # 关于类的特殊情况
# # 每个直接声明在类中的名称都是类属性(attribute)，可通过 class.attribute 来访问
# class Nutrimatic:
#     output="Something almost, but not quite, entirely unlike tea."
#     def request(self, beverage):
#         return self.output
# machine=Nutrimatic()
# mug=machine.request("Tea")
# print(mug)
# print(machine.output)
# print(Nutrimatic.output)
# # 三个 print 输出相同的内容
# # output 是类属性，即便在 class 内，也必须通过 self.output 来访问

# # # 不可变的真相

# # 不可变的值：int/float/str/tuple
# eggs = 12
# carton = eggs
# print(eggs is carton)
# eggs += 1
# print(eggs is carton)
# print(eggs)
# print(carton)
# # 可变类型的值可以在原地修改，如list
# temps = [87, 76, 79]
# highs = temps
# print(temps is highs)
# temps += [81]
# print(temps is highs)
# print(highs)
# print(temps)

# # # 赋值传递

# # python不使用值传递，也不使用引用传递
# # ?值和绑定到它们的名称都不会被移动，相反，每个值都通过赋值被绑定到参数
# def greet(person):
#     print(f"Hello, {person}.")
# my_name = "Jason"
# greet(my_name)
# # 内存中只有"Jason"的一个副本，赋值不会复制值
# # 调用函数 find_lowest 时，把 temps 绑定的值赋值给参数 temperatures 时
# # 因为列表是#可变#的，实际上只是为列表创建了一个别名！
# # 在函数内对 temperatures 的任意更改都可以从绑定到同意列表的其他名称中看到
# def find_lowest(temperatures):
#     temperatures.sort()
#     print(temperatures[0])
# temps = [85, 76, 79, 72, 81]
# find_lowest(temps)
# print(temps)

# # 函数不应该有副作用
# # 任何作为参数传递给函数的值都不应该被直接更改
# # 这样的参数，需要#显式#地对原始值进行复制
# # 我们使用sorted生成了新列表，而不是在原始列表上进行.sort操作
# # 这样维持了temperatures和temps保持不变
# def find_lowest(temperatures):
#     sorted_temps = sorted(temperatures)
#     print(sorted_temps[0])
# temps = [85, 76, 79, 72, 81]
# find_lowest(temps)
# print(temps)

# # 集合和引用

# # 所有集合/列表的元素，都是引用
# # 就像名称被绑定到值，元素也绑定到值
# # 这样的绑定称为#引用#
# board = [["-"] * 3] * 3
# print(board)
# board[1][0]="x"
# for row in board:
#     print(f"{row[0]} {row[1]} {row[2]}")
# # 在 board = [["-"] * 3] * 3 中
# # ["-"] * 3 是包含3个 "-" 字符串的列表
# # 字符串不可变，不能原地修改
# # board[1][0]重新被绑定到 "x" 不会影响board[1][1]和board[1][2]
# # 外层的列表由3个列表项组成
# # 同一列表项被使用了3次，所以一个可变列表项有3个名称
# # board[1][0]重新被绑定到 "x" 会影响board[0][0]和board[2][0]

# # 需要确保每一行都引用一个单独的值
# board = [["-"] * 3 for _ in range(3)]
# board[1][0] = "x"
# for row in board:
#     print(f"{row[0]} {row[1]} {row[2]}")
# # 使用列表推导式可以定义值相同但身份不同的三个列表

# # 集合中的元素和变量的名称没有区别
# # 元组不可变，但其中的元素可变
# score_team_1 = [100, 95, 120]
# score_team_2 = [45, 30, 10]
# score_team_3 = [200, 35, 190]
# scores = (score_team_1, score_team_2, score_team_3)
# score_team_1[0] = 300
# print(scores[0])
# scores[0][0] = 400
# print(scores[0])

# # 浅拷贝
# # copy()可以将名称绑定到一个可变值的#副本#上
# class Taco:
#     def __init__(self, toppings):
#         self.ingredients = toppings
#     def add_sauce(self, sauce):
#         self.ingredients.append(sauce)
# default_toppings = ["Lettuce", "Tomato", "Beef"]
# mild_taco = Taco(default_toppings)
# hot_taco = Taco(default_toppings)
# hot_taco.add_sauce("Salsa")
# print(f"Hot: {hot_taco.ingredients}")
# print(f"Mild: {mild_taco.ingredients}")
# print(f"Default: {default_toppings}")
# # default_toppings, hot_taco.ingredients, mild_taco.ingredients
# # 都是内存中同一个值的别名
# # 因此要确保分配一个可变值的副本，可以使用copy模块中的copy()函数
# import copy
# class Taco:
#     def __init__(self, toppings):
#         self.ingredients = copy.copy(toppings)
#     def add_sauce(self, sauce):
#         self.ingredients.append(sauce)
# default_toppings = ["Lettuce", "Tomato", "Beef"]
# mild_taco = Taco(default_toppings)
# hot_taco = Taco(default_toppings)
# hot_taco.add_sauce("Salsa")
# print(f"Hot: {hot_taco.ingredients}")
# print(f"Mild: {mild_taco.ingredients}")
# print(f"Default: {default_toppings}")

# # 深拷贝
# import copy
# class Taco:
#     def __init__(self, toppings):
#         self.ingredients = copy.copy(toppings)
#     def add_sauce(self, sauce):
#         self.ingredients.append(sauce)
# default_toppings = ["Lettuce", "Tomato", "Beef"]
# mild_taco = Taco(default_toppings)
# hot_taco = copy.copy(mild_taco)
# hot_taco.add_sauce("Salsa")
# print(f"Hot: {hot_taco.ingredients}")
# print(f"Mild: {mild_taco.ingredients}")
# print(f"Default: {default_toppings}")
# # 浅拷贝只拷贝了对象，但对象包含同一列表值的引用
# # 深拷贝将创建对象副本，以及对象引用的任何#可变值#的副本
# import copy
# class Taco:
#     def __init__(self, toppings):
#         self.ingredients = copy.copy(toppings)
#     def add_sauce(self, sauce):
#         self.ingredients.append(sauce)
# default_toppings = ["Lettuce", "Tomato", "Beef"]
# mild_taco = Taco(default_toppings)
# hot_taco = copy.deepcopy(mild_taco)
# hot_taco.add_sauce("Salsa")
# print(f"Hot: {hot_taco.ingredients}")
# print(f"Mild: {mild_taco.ingredients}")
# print(f"Default: {default_toppings}")
# 一般来说copy适用于只修改外层（增删元素），deepcopy适用于需要修改深层可变子对象

# # # 隐式类型转换和显式类型转换

# # 隐式类型转换(coercion)，python自行完成的转换
# print(42.5)  # coerces to a string
# x = 5 + 1.5  # coerces to a float
# y = 5 + True  # coerces to an int
# # 显式类型转换(conversion)，通过代码进行的转换
# life_universe_everything = "42"
# answer = float(life_universe_everything)
# print(type(answer))
# print(answer)
# # 每种数据类型都是一个类的实例，每个类都定义了自己的初始化器
# # 显示类型转换，本质是将原对象作为__init__()的参数，创建新类型的实例，并绑定到名称

# # # 匈牙利命名法
# def calculate_age(intBirthYear, intCurrentYear):
#     intAge = intCurrentYear - intBirthYear
#     return intAge
# def calculate_third_age_year(intCurrentAge, intCurrentYear):
#     floatThirdAge = intCurrentAge / 3
#     floatCurrentYear = float(intCurrentYear)
#     floatThirdAgeYear = floatCurrentYear - floatThirdAge
#     intThirdAgeYear = int(floatThirdAgeYear)
#     return intThirdAgeYear
# strBirthYear = "1985"
# intBirthYear = int(strBirthYear)
# strCurrentYear = "2010"
# intCurrentYear = int(strCurrentYear)
# intCurrentAge = calculate_age(intBirthYear, intCurrentYear)
# intThirdAgeYear = calculate_third_age_year(intCurrentAge, intCurrentYear)
# print(intThirdAgeYear)
# # 如果充分利用python语言的动态类型系统，并抑制将每个中间步骤存储在变量中的冲动
# # 代码将更#紧凑#
# # duck_typing_feels_better
# def calculate_age(birth_year, current_year):
#     return current_year - birth_year
# def calculate_third_age_year(current_age, current_year):
#     return int(current_year - (current_age / 3))
# birth_year = "1985"
# birth_year = int(birth_year)
# current_year = "2010"
# current_year = int(current_year)
# current_age = calculate_age(birth_year, current_year)
# third_age_year = calculate_third_age_year(current_age, current_year)
# print(third_age_year)
# # 不要尝试使用某种方式"记住"每个名称所绑定的值的类型！

# # # 术语回顾
# # 别名/alias：将可变值绑定到多个名称，
#     # 对绑定到一个名称的可变值进行的修改将对绑定到该可变值的所有名称可见
# # 赋值/assignment：将值绑定到名称。赋值操作不会复制数据
# # 绑定/bind：在名称和值之间创建引用。名称具有作用域，但没有类型
# # 隐式类型转换/coercion：python隐式地将一个值从一种类型转换为另一种类型
# # 显式类型转换/conversion：程序员通过代码将值从一种类型转换为另一种类型
# # 复制/copy：依据一个值的数据在内存中创建一个新值
# # 数据/data：存储在值中的信息。你可能会在其他值中存储任何给定数据的副本
# # 深拷贝/deep_copy：既复制对象到新值，又将对象中引用的所有数据复制到新值
# # 身份/identity：名称被绑定到内存中的特定位置
#     # 两个名称共享身份，它们被绑定到内存中的同一个值
# # 不可变/immutable：不能原地修改
# # 可变/mutable：可以原地修改
# # 修改/mutate：原地修改一个值
# # 名称/name：内存中值的引用，通常认为是python中的变量
#     # 名称必须始终绑定到值。名称有作用域，但没有类型
# # 重新绑定/rebind：将现有名称绑定到另一个的值
# # 引用/reference：名称与值之间的关联
# # 作用域/scope：变量名称在代码中可以访问的部分
# # 浅拷贝/shallow_copy：将对象复制到新值，但不将对象中引用的所有数据复制到新值
# # 类型/type：定义如何解释原始值
# # 值/value：内存中数据的唯一副本。必须有对值的引用，否则值将被删除
#     # 值具有类型，但没有作用域
# # 变量/variable：名称和名称所引用的值的组合
# # 弱引用/weakref：不会增加对值的引用计数的引用
# # 本书通常使用名称而非变量
# # 不说改变什么，而说(重新)绑定一个名称，或修改一个值
# # 赋值绝非复制，前者实际上是将一个名称绑定到一个值
