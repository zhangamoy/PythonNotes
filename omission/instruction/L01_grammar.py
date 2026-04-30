#!/usr/bin/env python3
# import math
# from string import Template

# Run via <F5> or terminal: python *.py

# # Statements & Expressions
# name=input("What is your name?")
# print("Hello, "+name+"!")
# # Expressions evaluate; statements execute.
# # Use semicolons only to delimit multiple statements on a single line.

# # Clause: indent
# name = "Morgan"
# if name != "":
#     message = "Hello, " + name + "!"
#     print(message)
# else:
#     pass # 空语句，pass关键字
# print("I am a computer.")
# # Compound statements consist of one or more 'clauses.'
# # A clause consists of a header and a 'suite'.
# # The suite must be indented relative to the header.

# 声明变量
# Python是动态类型语言，是强类型语言
# 使用前先声明
# 没有正式定义的常量

# # # 数学操作

# # 类型
# # 整型int, 默认十进制, 其它进制: 0b/0o/0x
# # 浮点型float, float("-inf")表示负无穷, float("nan")表示无效数字
# # 复数型complex, e.g. 24+42j
# # import Decimal/Fraction以存储小数点固定的进制数/分数, e.g. Fraction(1,3); Decimal("0.333")

# # 运算符
# print(-42)
# print(abs(-42))  # absolute
# print(40 + 2)
# print(44 - 2)
# print(21 * 2)
# print(680 / 16)
# print(680 // 16)  # floor division
# print(1234 % 149)  # modulo
# print(7**2)  # exponent
# print((9 + 5) * 3)

# # 增强赋值运算符 augmented_assignment_operators
# foo = 10
# foo += 10
# foo -= 5
# foo *= 16
# foo //= 5
# foo /= 4
# foo **= 2
# foo %= 51
# # divmod(a,b)返回元组，包含商和余数

# # 位运算符 bitwise_operators
# print(9 & 8)  # AND
# print(9 | 8)  # OR
# print(9 ^ 8)  # XOR
# print(~8)
# print(1 << 3)  # 0001->1000
# print(8 >> 3)  # 1000->0001

# # math模块
# print(math.pi)
# print(math.tau)
# print(math.e)
# print(math.inf)
# print(math.nan)  # Not-a-Number

# # 角度、弧度和三角函数
# distance_ft = 65
# angle_deg = 74
# angle_rad = math.radians(angle_deg)
# height_ft = distance_ft * math.tan(angle_rad)
# height_ft = round(height_ft, 1)
# print(height_ft)

# # # 逻辑操作

# # 条件语句 conditional_statements
# command = "greet"
# if command == "greet":      # Clause 1, Header
#     print("Hello!")         # Clause 1, Suite
# elif command == "exit":     # Clause2
#     print("Goodbye!")
# else:                       # Clause3
#     print("I don't understand.")

# # 比较运算符 comparison_operators
# score = 98
# high_score = 100
# print(score == high_score)  # 还包括!=, <, >, <=, >=

# # 布尔运算符 boolean_identity_operators
# spam = True
# eggs = False
# potatoes = None
# if spam is True:
#     print("We have spam.")
# if spam is not False:
#     print("I DON'T LIKE SPAM!")
# if spam:#这是好的
#     print("Spam, spam, spam, spam...")
# if eggs is False:
#     print("We're all out of eggs.")
# if eggs is not True:
#     print("No eggs, but we have spam, spam, spam, spam...")
# if not eggs:#这是好的
#     print("Would you like spam instead?")
# if potatoes is None:#这是好的
#     print("Yum")
# if potatoes is not None:#这是好的
#     print("Yes, we have no potatoes")
# if eggs is spam:# which is
#     print("This won't work.")
# # 建议只用is比较是否为none，其它建议直接用表达式/变量名本身

# # 真实性 truthiness
# answer = 42
# if answer:
#     print("Evaluated to True.")
# print(bool(answer))
# # 表达式为True被认为是真实的，否则是虚假的
# # 常量None、表示0的值，以及空集都被认为是虚假的

# # 逻辑运算符 logical_operators
# spam = True
# eggs = False
# if (not eggs) and spam:
#     print("But I DON'T LIKE SPAM!")
# # 包括and, or, not运算符
# score = 98
# high_score = 100
# print(score != high_score)
# print(not score == high_score)
# # 以上两句等价，not能反转一切，但可能牺牲可读性

# # 海象运算符 walrus
# if (eggs:=7+5)==12:
#     print("We have one dozen eggs.")
# print(eggs)
# # 赋值的同是在表达式中使用变量，主要括号的必要性
# # 可以使变量称为外部作用域中的有效变量
# # 不要滥用海象运算符，牺牲了可读性

# # # 字符串

# # 字符串字面量 string_literals
# danger = 'Cuidaao, llamas!'
# danger = "Cuidaao, llamas!"
# danger = '''Cuidaao, llamas!'''
# danger = """Cuidaao, llamas!"""
# # 单双引号是相同的，但建议风格统一
# quote = "Shout \"Cuidado, llamas!\""
# quote = 'Shout "Cuidado, llamas!"'
# question = 'What do you mean, "it\'s fine"?'
# # 相比于用反斜线，区别单双引号的用法更具有可读性，但有时候反斜线是必要的
# question = """What do you mean, "it's fine"?"""
# # 使用三重引号可以完全抛弃反斜线"\"，还能定义多行字符串字面量￬
# parrot = """\
# This parrot is no more!
# He has cased to be!
# He's expired
#     and gone to meet his maker!
# He's a stiff!
# Bereft of life,
#     he resets in peace!"""
# print(parrot)
# # 三重引号内所有字符，包括空格和换行符，第一个\是一种奇怪的惯例

# # 原始字符串 raw_strings
# print(r"I love backslashes: \ Aren't they cool?")
# # 禁用了转义字符
# print("A\nB")
# print(r"A\nB")
# # 通常我们用\n代表换行符
# # 原始字符串对正则表达式特别有用

# # 格式化字符串 formatting_strings
# in_stock = 0
# print("This cheese shop has " + str(in_stock) + " types of cheese.")
# print(f"This cheese shop has {in_stock} types of cheese.")
# # f指示python解释和评估字符串中被花括号包裹的表达式，包括数字、函数调用、条件表达式等等
# print(f"{5+5=}")
# # 甚至在末尾用"="同时显示表达式及结果

# answer = 42
# print(f"{answer}")
# print(f"{{{answer}}}")
# print(f"{{{{{answer}}}}}")
# print(f"""The unicode of " is: {ord('"')}.""")
# # 不能使用转义符号，用{{}}表示花括号字符，为了使用单双引号，我们用到了三重引号
# newline_ord=ord('\n')
# print(f"{newline_ord}")
# # 还可以先将字符赋予给变量

# spam = 1234.56789
# print(f"{spam:=^+15,.2f}")
# spam = 42
# print(f"{spam:#07x}")
# spam='Hi!'
# print(f"{spam:-^20}")
# # 格式规范以冒号':'开头，后跟一个或多个标志
# # 对齐标志：<、>、^、=
# # 符号标志：+、-、' '
# # 替代形式：#
# # 前导零：0后跟
# # 宽度标志
# # 分组标志：,、_
# # 精度标志：.
# # 类型标志：b、c、d、x、e、f、g
# # 在表达式后可以有三种特殊标志之一：!r、!a、!s

# # 模板字符串 template_strings
# # from string import Template是必要的
# s = Template("$greeting, $user!")
# # 创建模板s并用$给字段命名
# print(s.substitute(greeting="Hi", user="Jason"))
# # 然后将参数传给两个字段，代入模板中
# s = Template("A ${thing}ify subscription costs $$$price/mo.")
# print(s.substitute(thing="Code", price=19.95))
# # 用花括号表示字段为单词的一部分，用$$表示美元符号本身

# # 字符串转换
# # str()返回值的可读表示形式
# # repr()返回值的规范字符串表示形式
# # ascii()和repr()类似，但返回的字符串字面量是ASCII兼容的

# # 字符串拼接 concat_strings
# greeting = "Hello"
# name = "Jason"
# message = greeting + ", " + name + "!"
# print(message)
# message = "".join((greeting, ", ", name, "!"))
# print(message)
# # 用join()方法接收字符串#元组#（用括号包裹的类数组结构，所以有两组括号）
# # 通常f-字符串最快，join()其次，+最慢

# # # 函数
# def tell_joke(joke_type):
#     # 声明函数，函数头以:结尾
#     # def function(parameter):
#     if joke_type == "funny":
#         print("How can you tell an elephant is in your fridge?")
#         print("There are footprints in the butter!")
#     elif joke_type == "lethal":
#         print("Wenn ist das Nunstück git und Slotermeyer?")
#         print("Ja! Beiherhund das Oder die Flipperwaldt gersput!")
#     else:
#         print("Why did the chicken cross the road?")
#         print("To get to the other side!")
#     # 函数的套件，用缩进表示
# tell_joke("funny")
# # 调用函数
# # function(argument)

# # # 类和对象 Class & Object
# # 定义类
# # class Class_name:
# class Joke:

#     # 类的套件，初始化器/构造函数，是一个名为__init__()的成员函数或方法，至少有一个参数self
#     def __init__(self, joke_type):
#         if joke_type == "funny":
#             self.question = "How can you tell an elephant is in your fridge?"
#             self.anwser = "There are footprints in the butter!"
#         elif joke_type == "lethal":
#             self.question = "Wenn ist das Nunstück git und Slotermeyer?"
#             self.anwser = "Ja! Beiherhund das Oder die Flipperwaldt gersput!"
#         else:
#             self.question = "Why did the chicken cross the road?"
#             self.anwser = "To get to the other side!"

#     # 类中的函数称为方法，至少接受一个参数self
#     def tell(self):
#         print(self.question)
#         print(self.anwser)

# # 用Class()来创建一个新的实例/对象，同时需要向初始化器传递self以外的必要参数，新对象存储在变量中
# # var=Class(argument)
# lethal_joke = Joke("lethal")
# # 用.在对象内部调用方法
# # var.method()
# lethal_joke.tell()

# # # 异常处理 try_except
# num_from_user = input("Enter a number.")
# # 用try让异常显示
# try:
#     num = int(num_from_user)
# # 用except捕获异常，并给出解决方案
# except ValueError:
#     print("You didn't enter a valid number.")
#     num = 0
# print(f"Your number squared is {num**2}.")

# # # 元组和列表 tuple & list
# # 列表用方括号将多个元素囊括，用逗号分隔
# cheese = ["Red Leicester", "Tilsit", "Caerphilly", "Bel Paese"]
# print(cheese[1])
# cheese[1] = "Cheddar"
# print(cheese[1])
# # 元组用圆括号将多个元素囊括，用逗号分隔
# answers = ("Sir Lancelot", "To seek the holy grail", 0x0000FF)
# print(answers[0])
# answers[0] = "King Arthur"  # 报错
# # 列表可变，元组不可变
# # 不同类型元素集合，用元组；同类型元素集合（同构集合），用列表

# # # 循环 loop

# while循环 while_loop
# n = 0
# # while expression:
# while n < 10:
#     # 如果expression为True便执行套件内语句，并重新判断expression，直到False停止
#     n += 1
#     print(n)

# # 循环控制 loop_control
# # 理论上这个循环会无限重复
# while True:
#     command = input("Enter command: ")
#     # 除非有可能break结束循环
#     if command == "exit":
#         break
#     # 用continue则能直接开始下一次循环
#     elif command == "sing":
#         print("La la LAAAAA")
#         continue
#     print("Command unknown.")

# # for循环 for_loop
# # 遍历给定范围、列表、集合中的每一项
# # for ... in range
# # for each ...
# for i in range(1, 11):
#     print(i)

# # # 结构模式匹配

# # 文本模式 pattern_match
# lunch_order = input("What would you like for lunch?")
# # 3.10+的Python才支持match
# match lunch_order:
#     case "pizza":
#         print("Pizza time!")
#     case "sandwich":
#         print("Here's your sandwich.")
#     case "taco":
#         print("Taco, taco, TACO, tacotacotaco!")
#     # 竖线分隔，从而覆盖多种可能的值
#     case "salad" | "soup":
#         print("Eating healthy, eh?")
#     # 下划线通配符匹配任何值，这称为回退case，放在最后
#     case _:
#         print("Yummy.")

# # 捕获模式
# # 案例1
# lunch_order = input("What would you like for lunch?")
# match lunch_order:
#     case "salad" | "soup":
#         print("Eating healthy, eh?")
#     # 将lunch_order的值捕获为order，另一种回退case
#     case order:
#         print(f"Enjoy your {order}.")

# # 案例2
# lunch_order = input("What would you like for lunch?")
# if " " in lunch_order:
#     # 将字符串用" "隔开，分成两个部分，储存在列表lunch_order中
#     lunch_order = lunch_order.split(maxsplit=1)
# match lunch_order:
#     # 如果lunch_order第二个部分是'ice cream'那就把第一部分捕获为flavor
#     case (flavor, "ice cream"):
#         print(f"Here's your very grown-up {flavor}...lunch.")

# # ?案例3
# # ?所有未限定的名称——即不含点号的简单变量名称——都将用于捕获
# # ?这意味着如果想使用某个变量的值，则该变量必须被限定
# # ?即必须在某个类或模块中使用点运算符访问它
# class Special:
#     TODAY = "lasagna"
# lunch_order = input("What would you like for lunch?")
# match lunch_order:
#     case Special.TODAY:
#         print("Today's special is awesome!")

# # 门卫语句
# # 额外的条件语句，必须满足才能匹配模式
# # 对于#捕获模式-案例2#，如果我们输入"rocky road ice cream"，因为有多个空格无法较好地匹配
# # 作为替代：
# lunch_order = input("What would you like for lunch?")
# if " " in lunch_order:
#     # 将字符串用" "隔开，分成两个部分，储存在列表lunch_order中
#     lunch_order = lunch_order.split(maxsplit=1)
# match lunch_order:
#     # 将lunch_order的值捕获为ice_cream，如果包含"ice cream"
#     # 为什么不写作  case ice_cream if 'ice cream' in lunch_order:  呢？
#     case ice_cream if "ice cream" in ice_cream:
#         # 用replace()和strip()只保留冰淇淋的口味
#         flavor = ice_cream.replace("ice cream", "").strip()
#         print(f"Here's your very grown-up {flavor}...lunch.")

