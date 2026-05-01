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

# python允许在函数中实现另一个函数
spam=True
def order():
    eggs=12
    def cook():
        nonlocal eggs
        if spam:
            print("Spam!")
        if eggs:
            eggs-=1
            print("...and eggs.")
    cook()
order()
# 函数内只是访问全局名称 spam 并不需要做额外的事情
# 但重新赋值则会定义新名称，并在函数内覆盖全局名称
# nonlocal 关键字允许内部函数使用定义在外部函数中的名称
# 这称为嵌套作用域或封闭作用域
# 所以若没有 nonlocal ，在 cook() 内给 eggs 赋值并在赋值前使用，就会报错

# 作用域解析顺序 LEGB
    # Local: 局部作用域
    # Enclosing-function locals: 外部函数的局部作用域
    # Global: 全局作用域
    # Built-in: 内置作用域
# 当使用 Global 或 Nonlocal 关键字时，改变了作用域解析顺序

# 关于类的特殊情况 
# 每个直接声明在类中的名称都是类属性(attribute)，可通过 class.attribute 来访问
class Nutrimatic:
    output="Something almost, but not quite, entirely unlike tea."
    def request(self, beverage):
        return self.output
machine=Nutrimatic()
mug=machine.request("Tea")
print(mug)
print(machine.output)
print(Nutrimatic.output)
# 三个 print 输出相同的内容
# output 是类属性，即便在 class 内，也必须通过 self.output 来访问
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 