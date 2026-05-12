# # # # 错误和异常 # # # #

# 异常有助于别想更好的代码

# --------------------------------------------------------------------------------------------
# # # python中的异常

# # 异常：计算机正常处理的中断，通常由错误条件引起，可以由程序的另一部分处理

# # 案例：猜数字游戏
# import random

# def generate_puzzle(low=1, high=100):
#     ''' 生成随机数
#     '''
#     print(f"I'm thinking of a number between {low} and {high}...")
#     return random.randint(low, high)

# def make_guess(target):
#     ''' 比较输入与目标
#     '''
#     guess = int(input("Guess: "))
#     if guess == target:
#         return True
#     if guess < target:
#         print("Too low.")
#     elif guess > target:
#         print("Too high.")
#     return False

# def play(tries=8):
#     ''' 猜数字游戏，限定猜测机会<=tries
#     '''
#     target = generate_puzzle()
#     while tries > 0:
#         if make_guess(target):
#             print("You win!")
#             return
#         tries -= 1
#         print(f"{tries} tries left.")
#     print(f"Game over! The answer was {target}.")

# if __name__ == "__main__":
#     play()

# # 测试：对你的代码做糟糕的事情
# # 即输入它不期望或不理解的内容

# --------------------------------------------------------------------------------------------
# # # 阅读异常信息

# # 发生异常后出现的输出 Traceback 是异常信息
# # 包含发生错误的详细信息、错误发生的行，以及整个调用栈
# # 需要根据调用栈确定出错的位置
# # 建议从底部开始阅读

# # Traceback (most recent call last):
# #   File "C:\Program Files\Python39\lib\runpy.py", line 197, in _run_module_as_main
# #     return _run_code(code, main_globals, None,
# #   File "C:\Program Files\Python39\lib\runpy.py", line 87, in _run_code
# #     exec(code, run_globals)
# #   File "c:\Users\53596\.vscode\extensions\ms-python.debugpy-2026.6.0-win32-x64\bundled\libs\debugpy\__main__.py", line 71, in <module>
# #     cli.main()
# #   File "c:\Users\53596\.vscode\extensions\ms-python.debugpy-2026.6.0-win32-x64\bundled\libs\debugpy/..\debugpy\server\cli.py", line 542, in main
# #     run()
# #   File "c:\Users\53596\.vscode\extensions\ms-python.debugpy-2026.6.0-win32-x64\bundled\libs\debugpy/..\debugpy\server\cli.py", line 361, in run_file
# #     runpy.run_path(target, run_name="__main__")
# #   File "c:\Users\53596\.vscode\extensions\ms-python.debugpy-2026.6.0-win32-x64\bundled\libs\debugpy\_vendored\pydevd\_pydevd_bundle\pydevd_runpy.py", line 310, in run_path
# #     return _run_module_code(code, init_globals, run_name, pkg_name=pkg_name, script_name=fname)
# #   File "c:\Users\53596\.vscode\extensions\ms-python.debugpy-2026.6.0-win32-x64\bundled\libs\debugpy\_vendored\pydevd\_pydevd_bundle\pydevd_runpy.py", line 127, in _run_module_code
# #     _run_code(code, mod_globals, init_globals, mod_name, mod_spec, pkg_name, script_name)
# #   File "c:\Users\53596\.vscode\extensions\ms-python.debugpy-2026.6.0-win32-x64\bundled\libs\debugpy\_vendored\pydevd\_pydevd_bundle\pydevd_runpy.py", line 118, in _run_code
# #     exec(code, run_globals)
# #   File "C:\Users\53596\python\capri\omission\instruction\L06_error.py", line 44, in <module>
# #     play()
# #   File "C:\Users\53596\python\capri\omission\instruction\L06_error.py", line 36, in play
# #     if make_guess(target):
# #   File "C:\Users\53596\python\capri\omission\instruction\L06_error.py", line 22, in make_guess
# #     guess = int(input("Guess: "))
# # ValueError: invalid literal for int() with base 10: 'fifty'

# # ValueError 被引发，因为值 'fifty' 被传递给 int() 函数
#     # ValueError: invalid literal for int() with base 10: 'fifty'
# # 换句话说，python无法使用 int() 函数将字符串 'fifty' 转换为整数

# # 往上两行信息告诉出错的位置是 L06_error.py 文件中第22行的 make_guess() 函数
#     #   File "C:\Users\53596\python\capri\omission\instruction\L06_error.py", line 22, in make_guess
#     #     guess = int(input("Guess: "))
# # 并摘取了具体出问题的语句

# # 有时候问题就在这里，还有可能在调用栈中更高层代码中的错误导致的
#     #   File "C:\Users\53596\python\capri\omission\instruction\L06_error.py", line 36, in play
#     #     if make_guess(target):
# # 譬如将错误的数据传递给了参数（在本案例中并不是）

# # 异常信息的第一行总是一样的
# # Traceback (most recent call last):

# # 强调！最近执行的代码总是最后列出！


# --------------------------------------------------------------------------------------------
# # # 捕获异常：LBYL和EAFP

# # 先看后跳 Look Before You Leap
# # 例如，尝试将输入转换为整数之前测试它们
# # 重写 make_guess() 函数

# def make_guess(target):
#     # LBYL的哲学 ￬
#     guess = None
#     while guess is None:
#         guess = input("Guess: ")
#         if guess.isdigit():
#             guess = int(guess)
#         else:
#             print("Enter an integer.")
#             guess = None
#     # LBYL的哲学 ￪
#     pass

# # 请求宽恕比请求许可更容易 Easier to Ask Forgiveness than Permission
# # 例如，接受错误，并用 try 语句处理异常情况
# # 重写 make_guess() 函数

# def make_guess(target):
#     # EAFP的哲学 ￬
#     guess = None
#     while guess is None:
#         try:
#             guess = int(input("Guess: "))
#         except ValueError:
#             print("Enter an integer.")
#     # EAFP的哲学 ￪
#     pass

# # 在这里，LBYL 和 EAFP 都是有效的，但前者效率不高
# # 正确的情况下 LBYL 要先运行 isdigit() 再运行 int() ，处理 guess 字符串两次
# # 而 EAFP 只需要一次
# # 而且它的策略更好理解：
# # 与预测每个可能的错误输入相比，只需要可能出现的异常、捕获并相应处理即可

# --------------------------------------------------------------------------------------------
# # # 多异常处理

# # try 语句可以在复合语句中处理多种异常
# # 案例：计算平均数

# class AverageCalculator:
#     def __init__(self):
#         self.total = 0
#         self.count = 0

#     def __call__(self, *values):
#         if values:
#             for value in values:
#                 self.total += float(value)
#                 self.count += 1
#         return self.total / self.count

# average = AverageCalculator()
# values = input("Enter scores, seperated by spaces:\n    ").split()
# try:
#     print(f"Average is {average(*values)}.")
# except ZeroDivisionError:  # 用户不传递值，count = 0
#     print("ERROR: No values provided.")
# except (ValueError, UnicodeError):  # 输入可能无法转换为浮点值，多个错误用元组表示
#     print("ERROR: All inputs should be numeric.")

# # 现实世界中可能将 try 语句放在 __call__() 方法内部，这么做其实不太 pythonic

# --------------------------------------------------------------------------------------------
# # # 当心尿布反模式

# # 空的 except 子句也会起作用，但这很糟糕

# try:
#     some_scary_function()
# except:  # Do not use bare `except`
#     print("An error occurred. Moving on!")

# # 这是一种极为邪恶的反模式：
# # 所有有关实际错误的宝贵的上下文都被'尿布'捕获，永远看不到光明，
# # 也不会进入问题追踪器。当异常随后发生时，堆栈跟踪指向第二个错误发生的位置，
# # 而不是try块内部的实际错误

# # 更糟的是，如果程序不再引发第二个异常，而你仍然尝试在第一个异常无效的状态下工作
# # 那么通常会出现大量奇怪的现象

# # 案例：问候 - 恶魔般的副作用

# def greet():
#     name = input("What's your name?")
#     print(f"Hello, {name}.")

# while True:
#     try:
#         greet()
#         break
#     except:
#         print("Error caught")

# # 当使用快捷键退出程序时，你被困在了 KeyboardInterrupt 的死循环中
# # KeyboardInterrupt 异常本身没有从 Exception 类继承
# # 所以修改 except Exception: 可以从死循环中逃脱
# # 虽然它仍然是一种 '尿布反模式'

# # 强调！一定要明确地捕获特定的异常类型！


# --------------------------------------------------------------------------------------------
# # # 抛出异常

# # 代码中存在无法自动恢复的问题时，可以主动引起抛出异常
# # 案例：平均数


# def average(number_string):
#     total = 0
#     skip = 0
#     values = 0
#     for n in number_string.split():
#         values += 1
#         try:
#             total += float(n)
#         except ValueError:  # 如果部分不能转数字引发异常并跳过
#             skip += 1
#     if skip == values:  # 如果跳过了所有值，引发另一个 ValueError
#         raise ValueError("No valid numbers provided.")
#     elif skip:  # 否则输出有用的信息并继续
#         print(f"<!> Skipped {skip} invalid values.")
#     return total / values

# while True:
#     try:
#         line = input("Enter numbers (space delimited):\n ")
#         avg = average(line)
#         print(avg)
#     except ValueError:  # 如果没有这个 try 语句，上面引发的抛出便会终止程序
#         print("No valid numbers provided.")

# # 抛出异常会导致函数立即退出，因此如果用户传入空字符串时，不必担心 return 报错

# --------------------------------------------------------------------------------------------
# # # 使用异常

# # 异常可以直接使用和提取信息的对象
# # 可以使用异常来处理访问字典中的值的逻辑，而不需要事先知道指定的键是否有效
# # 案例：电子邮件地址簿

# friend_emails = {
#     "Anne": "anne@example.com",
#     "Brent": "brent@example.com",
#     "Dan": "dan@example.com",
#     "David": "david@example.com",
#     "Fox": "fox@example.com",
#     "Jane": "jane@example.com",
#     "Kevin": "kevin@example.com",
#     "Robert": "robert@example.com",
# }

# def lookup_email(name):
#     try:
#         return friend_emails[name]
#     except KeyError as e:
#         print(f"<No entry for friend {e}>")

# name = input("Enter name to look up: ")
# email = lookup_email(name)
# print(f"Email: {email}")

# # ? 用 as e 捕获异常键，并在之后，用 str(e) 返回刚才尝试在字典中使用的键的值

# # 日志配置
# import logging
# from operator import add, sub, mul, truediv
# import sys

# # logging.basicConfig() 函数允许配置日志级别，并指定将日志写入哪个文件
# logging.basicConfig(filename="log.txt", level=logging.INFO)
# # 日志级别：DEBUG、INFO、WARNING、ERROR、CRITICAL
# # 设置 level=logging.INFO 可以记录 INFO 及以上级别的所有日志消息

# def calculator(a, b, op):
#     a = float(a)
#     b = float(b)
#     if op == "+":
#         return add(a, b)
#     elif op == "-":
#         return sub(a, b)
#     elif op == "*":
#         return mul(a, b)
#     elif op == "/":
#         return truediv(a, b)
#     else:
#         raise NotImplementedError(f"No operator {op}.")

# # NotImplementedError与NotImplemented不同，
# # 未实现的特殊方法都返回后者
# # 为实现的自定义方法或函数返回前者

# print("""CALCULATOR
# Use postfix notation.
# Ctrl+C or Ctrl+D to quit.
#       """)
# while True:
#     try:
#         equation = input(" ").split()
#         result = calculator(*equation)
#         print(result)
#     except NotImplementedError as e:
#         print("<!> Invalid operator.")
#         logging.info(e)
#     except ValueError as e:
#         print("<!> Expected format: <A> <B> <OP>.")
#         logging.info(e)
#     except TypeError as e:
#         print("<!> Wrong number of arguments. Use: <A> <B> <OP>.")
#         logging.info(e)
#     except ZeroDivisionError as e:
#         print("<!> Cannot divide by zero.")
#         logging.info(e)
#     except (KeyboardInterrupt, EOFError):
#         print("\nGoodbye.")
#         sys.exit(0)

# # 可以尝试运行，让异常被记录到log.txt中
# # INFO:root:could not convert string to float: '+'
# # INFO:root:calculator() takes 3 positional arguments but 5 were given
# # INFO:root:calculator() missing 1 required positional argument: 'op'
# # INFO:root:float division by zero
# # INFO:root:No operator @.

# # 冒泡
# # 前面方案中，任何意外异常都不会被记录
# # 理想情况下，预料外的异常都该被记录为 ERROR 级别，
# # 同时仍允许程序崩溃
# # 重新抛出已捕获的异常，这一行为被称为冒泡 Bubbling Up
#     except Exception as e:
#         logging.exception(e)
#         raise  # 将错误重新抛出
# # 这个新的子句必须出现在当前 try 语句的末尾
# # 它不是反尿布模式，因为捕获了实际发生的错误
# # 而且忽略了 KeyboardInterrupt 等不继承自 Exception 的非错误异常

# # ? 异常链
# # 通过这种方式，可以抛出一个新的异常，而不丢失已经获得的所有有用信息
# # 案例：地标

# cities = {
#     "SEATTLE": "WASHINGTON, USA",
#     "PORTLAND": "OREGON, USA",
#     "BOSTON": "MASSACHUSETTS, USA",
# }
# landmarks = {
#     "SPACE NEEDLE": "SEATTLE",
#     "LIBERTY SHIP MEMORIAL": "PORTLAND",
#     "ALAMO": "SAN ANTONIO",
# }

# def lookup_landmark(landmark):
#     landmark = landmark.upper()
#     try:
#         city = landmarks[landmark]
#         state = cities[city]
#     except KeyError as e:
#         # 使用 from e 指定这个异常 e 是由捕获的异常引起的
#         # 确保了异常信息会显示导致错误的原因
#         raise KeyError("Landmark not found.") from e
#     print(f"{landmark} is in {city}, {state}.")

# lookup_landmark("space needle")
# lookup_landmark("alamo")  # 异常，字典中缺少城市 san antonio
# lookup_landmark("golden gate bridge")  # 异常，字典中缺少地标 金门大桥

# # 即便没有添加 raise KeyError from e ，python 通常也会包含上下文
# # 两个异常信息之间会有一条更加晦涩且不太有用的消息：
# # During handling of the above exception, another exception occur red:
# # 所以即便不需要显式地使用异常链，养成这个好习惯也是很有必要的
# # 可以使用 raise e from None 显式地禁用异常链


# --------------------------------------------------------------------------------------------
# # # else和finally

# # try 语句和 except 子句让代码在任何情况下都可以运行
# # 除非调用 return 语句或利用 raise 语句的中断行为来退出函数
# # 此外，还有两个可选子句：
# # else 子句在没有异常时运行
# # finally 子句在任何情况下都会运行

# # 案例：平均数
# import math

# def average_string(number_string):
#     try:
#         numbers = [float(n) for n in number_string.split()]
#     except ValueError:
#         total = math.nan
#         values = 1
#     else:
#         total = sum(numbers)
#         values = len(numbers)
#     try:
#         average = total / values
#     except ZeroDivisionError:
#         average = math.inf
#     return average

# while True:
#     number_string = input("Enter space-delimited list of numbers:\n    ")
#     print(average_string(number_string))

# # total 和 values 是基于有效的假设计算的
# # 不在 except 子句中返回 math.nan 的原因：
# # 便于后续进行重构，它总是执行其余的数学运算，总产生有效结果
# # 即便添加一个 finally 子句，代码仍按预期运行

# # 即使 raise 或 return 也不能阻止 finally 子句运行
# # 案例：平均数（基于文件）
# def average_file(path):
#     file = open(path, "r")
#     try:
#         numbers = [float(n) for n in file.readlines()]
#     # 如果包含非数字的数据，捕获 ValueError
#     # 并引发链接异常，其中包含更多描述文件错误之处的具体信息
#     except ValueError as e:
#         raise ValueError
#         # raise ValueError("File contains non-numeric values.") from e
#     else:
#         try:
#             return sum(numbers) / len(numbers)
#         except ZeroDivisionError as e:
#             raise ValueError("Empty file.") from e
#     # 一定会运行，因为无论结果如何，文件都需要关闭！
#     # 注意，finally 子句实际是在 return 语句之前运行的
#     finally:
#         print("Closing file.")
#         file.close()

# print(average_file("omission/instruction/misc/numbers_good.txt"))
# # print(average_file("omission/instruction/misc/numbers_bad.txt"))
# # print(average_file("omission/instruction/misc/numbers_empty.txt"))
# # print(average_file("omission/instruction/misc/numbers_nonexistent.txt"))

# --------------------------------------------------------------------------------------------
# # # 创建异常

# # 自定义异常可以继承与需求接近的任何异常类，除 BaseException 之外
# # 默认可以继承 Exception 类
# # 满足至少两个条件，才建议定义自己的异常：
#     # 现有异常和自定义信息不能有效描述异常
#     # 需要捕获这个异常，而非任何相似的内置异常
#     # 将多次引发或捕获该异常

# # 案例：傻走
# class SillyWalkException(RuntimeError):
#     def __init__(self, message="Someone walked silly."):
#         super().__init__(message)
# def walking():
#     raise SillyWalkException("My walk has gotten rather silly.")
# try:
#     walking()
# except SillyWalkException as e:
#     print(e)

# --------------------------------------------------------------------------------------------
# # # 异常一览

# # 异常基类
# # BaseException 所有异常的基类，不要直接从这个类继承
# # Exception 所有错误类型异常的基类
# # ArithmeticError 与算术相关的错误类型异常的基类
# # LookupError 与在集合中查找值相关的任何错误类型异常的基类

# # 具体异常
# # AttributeError 是在访问或分配不存在的类属性时引发的
# # ImportError 是在import语句无法找到包、模块或模块中的名称时引发的
# # IndexError 是在索引超出顺序集合的范围时引发的
# # KeyError 是在字典中找不到键时引发的
# # KeyboardInterrupt 是在用户按下键盘组合键以中断正在运行的程序时引发的
# # MemoryError 是在Python内存不足时引发的
# # NameError 是在局部作用域或全局作用域中找不到名称时引发的
# # OSError 既是一个具体的错误，也是许多与操作系统相关的异常的基类
# # OverflowError 是在算术运算即将产生一个太大而无法表示或存储的结果时引发的
# # RecursionError 是在函数调用自身太多次时引发的
# # RuntimeError 是在捕获所有不属于其他异常类别的错误时引发的
# # SyntaxError 是在Python代码中有任何语法错误时引发的
# # SystemError 是在解释器发生内部错误时引发的，对于这些错误我们无能为力
# # SystemExit 是在调用sys.exit()时引发的，捕获该错误可能导致程序异常无法正常退出
# # TypeError 是在某个操作或函数尝试对错误类型的对象进行处理时引发的，如果不打算让你的函数处理接收到的某个特定值类型，这就是最好的异常
# # UnboundLocalError 在你尝试访问一个尚未分配值的局部名称时引发
# # ValueError 是在某个操作或函数尝试对类型正确但值错误的参数进行处理时引发的
# # ZeroDivisionError 是在尝试除以零时引发的
