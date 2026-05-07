# # # # 类和对象 # # # #

# # 面向对象编程(OOP)是一种将数据及相应的逻辑组织成对象的编程范式
# # python中的面向对象编程与函数式编程并不互斥
# # 使用对象编码<>面向对象编码
# # 面向对象编程中，类是创建对象的蓝图，创建的对象称为实例
# # 对象由成员变量(variable)和成员函数(function)组成
# # 在python中，它们被称为属性(attribute)和方法(method)
# # 实例具有属性形式的数据，具有作用域响应数据的方法
# # 类的目的是封装
#     # 数据和操作该数据的函数被绑定在一起
#     # 类的行为的实现与程序的其他部分无关(黑盒子)
# # 用于访问属性的方法称为getter，修改属性的方法称为setter
# # 两个重要的关系
#     # 组合/has-a关系：一个对象包含其它对象
#     # 继承/is-a关系：一个类继承并建立在另一个现有类之上


# --------------------------------------------------------------------------------------------
# # # 声明一个类

# # 类声明-隐式继承：一切类都(隐式地)继承自object类
# class SecretAgent:
#     pass
# # 类声明-显示继承
# class SecretAgent(object):
#     pass

# # 初始化器 __init__()
# # 初始化器是一个函数，来定义实例属性的初始值
#     # 这些实例属性是每个实例中都存在的成员变量
#     # 如果实例没有实例属性，则不用定义初始化器
# class SecretAgent:
#     def __init__(self, codename):
#         self.codename = codename
#         self._secrets = []
# # 初始化器的名称必须是__init__
#     # 必须接收至少一个参数，通常名为self，
#     # 该参数引用方法正在操作的实例
# # 实例属性是实例的一部分，需要对self使用点运算符访问
#     # 所有实例属性都在初始化器中声明
# # 初始化器不通过return关键字返回值
# # 每当创建新的类实例时，初始化器会自动调用
# mouse = SecretAgent("Mouse")
# armadillo = SecretAgent("Armadillo")
# fox = SecretAgent("Fox")
# 创建新实例时不需要传递任何内容给参数self

# # 构造器 __new__()
# # 在python中，构造函数__new__()负责实际在内存中创建实例
#     # 它是对象创建前自动调用的类中的唯一方法
#     # 除非需要对过程进行额外控制，否则不需要自定义构造函数
# def __new__(cls, *args, **kwargs):
#     return super().__new__(cls, *args, **kwargs)
# # 构造器隐式接收一个类作为第一个参数
# # 也许整个python编程生涯你都不必编写构造函数

# # 终结器 __del__()
# # 在类实例生命周期结束且类实例由垃圾回收器清理时被调用
# # 只要任何对类实例的引用仍存在，就不会调用终结器
# # 一个相当无用的终结器
# class SecretAgent:
#     def __init__(self, codename):
#         self.codename = codename
#         self._secrets = []
#         print(f"Hello, agent {self.codename}!")
#     def __del__(self):
#         print(f"Agent {self.codename} has been disavowed!")
# weasel = SecretAgent("Weasel")
# weasel_2 = weasel
# print("Arrivederci, Weasel!")
# del weasel
# print("Arrivederci, Weasel_2!")
# del weasel_2
# # # 手动创建新的类实例，绑定到名称weasel上，使用del关键字删除名称
# # 当不存在对名称weasel绑定的SecreatAgent类实例的引用时
# # 该实例才由垃圾回收器清理，垃圾回收器首先调用终结器
# # 注意：del只删除名称，而不删除值，


# --------------------------------------------------------------------------------------------
# # # 属性 attribute

# # 属于类或实例的变量，称为属性
# # 实例属性属于实例，值和实例一一对应，对其他实例不可用
# # 实例属性在类的初始化器中声明
# # 类属性属于类，被类和所有实例共享
# # 类属性在类的顶部声明
# class SecretAgent:
#     _codeword = ""
#     def __init__(self, codename):
#         self.codename = codename
#         self._secrets = []

# mouse = SecretAgent("Mouse")
# armadillo = SecretAgent("Armadillo")
# fox = SecretAgent("Fox")

# # 可以通过类或类实例访问并修改类属性
# # 如果在类本身中重新绑定或更改类属性，更改对所有实例生效
# SecretAgent._codeword = "Parmesan"
# print(armadillo._codeword)  # "Parmesan"
# print(mouse._codeword)  # "Parmesan"

# # 如果将值分配给实例的名称，则会#创建#具有相同名称的实例属性，更改仅对自己生效
# mouse._codeword = "Cheese"
# print(armadillo._codeword)  # "Parmesan"
# print(mouse._codeword)  # "Cheese"


# --------------------------------------------------------------------------------------------
# # # 作用域命名约定

# # 非公共属性，在属性名称前加下划线（如_secrets）
#     # 它不应该在类之外被修改、访问
#     # 实际上没有隐藏任何
# # 公共属性，不以下划线开头（如codename）
#     # 可以在外部被修改、访问
#     # 优于编写一个getter/setter方法对
#     # 当然也可以将属性定义为非公共的，并创建一个公共特性
# # 名称修饰，在名称前加双下划线
#     # 被修饰的名称无法从外部修改、访问（其实可以
#     # 用obj._Cls__attribute的方式访问
# class Message:
#     def __init__(self):
#         self.__format = "UTF-8"
# msg=Message()
# # print(msg.__format)  # AtrributeError
# print(msg._Message__format)

# # 用哪个？
# # 外部修改属性是否导致类中出现意外或负面行为？
# # Y:非公共属性  N:公共属性
# # 实践中很少使用这种模式，建议只在以下情况使用：
#     # 需要避免继承中的命名冲突
#     # 从外部访问属性将对类的行为产生异常可怕的影响
# # python没有私有类作用域，真正的秘密数据应该被加密，而不是仅对API隐藏


# --------------------------------------------------------------------------------------------
# # # 方法 method

# # 类的方法使封装成为可能

# # 实例方法
# # 属于实例本身的普通方法
# # 点运算符隐式地将mouse传递给self参数
# # 进而，坐标元组被传递给第二个参数secret
# class SecretAgent:
#     _codeword = ""
#     def __init__(self, codename):
#         self.codename = codename
#         self._secrets = []
#     def remember(self, secret):
#         self._secrets.append(secret)

# mouse = SecretAgent("Mouse")
# mouse.remember(("42.864025,-72.568511"))
# mouse.remember(("6.352081,20.368943"))
# print(mouse._secrets)

# # 类方法
# # 属于类的方法，这对于使用类属性很有用
# # 装饰器 @classmethod 确保了点运算符传递的参数 # 是类而不是实例 #
# # 因此，类方法可以直接在类或实例上调用，这和通过实例修改类属性不同
# class SecretAgent:
#     _codeword = ""
#     def __init__(self, codename):
#         self.codename = codename
#     @classmethod
#     def inform(cls,codeword):
#         cls._codeword=codeword

# mouse = SecretAgent("Mouse")
# fox = SecretAgent("Fox")
# SecretAgent.inform("The goose honks at midnight.")
# print(mouse._codeword)
# fox.inform("The duck quacks at midnight.")
# print(mouse._codeword)

# # 静态方法
# # 类中的常规函数，不访问实例属性或类属性
# # 通常这样的算法对于类的实现至关重要
# # 和普通函数的区别是，静态方法属于类的命名空间
# # 装饰器 @staticmethod 确保点运算符不会传递 class 或 instance
# class SecretAgent:
#     def __init__(self, codename):
#         self.codename = codename
#     @staticmethod
#     def inquire(question):
#         print("I know nothing.")
# mouse = SecretAgent("Mouse")
# mouse.inquire("What do you know?")


# --------------------------------------------------------------------------------------------
# # # 特性 property

# # 一种特殊的实例方法，允许编写getter和setter
# # 特性 # 看起来像 # 可以直接访问的实例属性
# # 特性允许你编写一致的接口，在其中你可以通过看起来像是对象的属性的形式来直接使用对象
# # Gemini：
# # 向后兼容，你可以先写普通属性，之后随时转成特性，不破坏 # 外部调用代码 #
# # 副作用是，隐藏了复杂度（读取、计算、查找），语法简洁

# # 先扩展SecretAgent类如下
# class SecretAgent:
#     _codeword = None

#     def __init__(self, codename):
#         self.codename = codename
#         self._secrets = []

#     def __del__(self):
#         print(f"Agent {self.codename} has been disavowed!")

#     def remember(self, secret):
#         self._secrets.append(secret)

#     @classmethod
#     def inform(cls, codeword):
#         cls._codeword = codeword

#     @staticmethod
#     def inquire(question):
#         print("I know nothing.")

#     # 使用类属性._codeword对字符串消息message进行加密/解密
#     # ord()将字符转为编码，chr()将编码转为字符，join()进行字符串拼接
#     @classmethod
#     def _encrypt(cls, message, *, decrypt=False):
#         code = sum(ord(c) for c in cls._codeword)
#         if decrypt:
#             code = -code
#         return "".join(chr(ord(m) + code) for m in message)

#     # 访问特性需要调用getter，将值分配给特性需要调用setter，使用del删除特性需要调用deleter
#     # 三个实例方法习惯命名为getx、setx、delx
#     # 这里定义为非公共方法，因为我们希望直接使用特性
#     # Gemini：说人话，就是我希望大家
#     # 使用instance.secret来访问_secrets[-1]
#     # 而不是用instance._getsecret（虽然也可以，但两个方法会对用户造成困惑）

#     # 先定义getter，不接受参数，返回._secrets列表中最后一项（或者None)
#     def _getsecret(self):
#         return self._secrets[-1] if self._secrets else None

#     # 定义setter，接收参数、加密，并存储在._secrets中，不返回值
#     def _setsecret(self, value):
#         self._secrets.append(self._encrypt(value))

#     # 定义deleter，不接受参数，不返回值
#     # 无论特性被显式、隐式地删除，该方法都会被调用
#     def _delsecret(self):
#         self._secrets = []

#     # 最后定义property本身，需要将三个实例方法传递给fget, fset, fdel关键字参数
#     secret = property(fget=_getsecret, fset=_setsecret, fdel=_delsecret)


# mouse = SecretAgent("mouse")
# mouse.inform("Parmesano")

# # 于是，特性可以像实例属性一样被使用
# print(mouse.secret)

# mouse.secret = "12345 Main Street"
# print(mouse.secret)
# print(mouse._encrypt(mouse.secret,decrypt=True))

# mouse.secret = "555-1234"
# print(mouse.secret)
# print(mouse._encrypt(mouse.secret,decrypt=True))

# del mouse.secret
# print(mouse.secret)

# # 没有必要逐一定义特性的三个部分，fget、fset、fdel有默认值为None
# # 如果不需要特定的错误用法，特别是在设计类或接口时，则错误用法应该明确地失败

# # 使用装饰器创建特性

# # 方法一　property()和装饰器
#     # 先声明特性，实例方法默认为None
#     secret = property()
#     # 用装饰器 @secret.getter 修饰，将下面的函数传递给 fget
#     @secret.getter
#     def secret(self):
#         return self._secrets[-1] if self._secrets else None
#     @secret.setter
#     def secret(self, value):
#         self._secrets.append(self._encrypt(value))
#     @secret.deleter
#     def secret(self):
#         self._secrets = []

# # 方法二　纯装饰器
#     # 用装饰器隐式地声明特性
#     @property
#     # 这么做相当于为新特性绑定了名称 secret ，且下方同名函数就是它的 getter
#     def secret(self):
#         return self._secrets[-1] if self._secrets else None
#     @secret.setter
#     def secret(self, value):
#         self._secrets.append(self._encrypt(value))
#     @secret.deleter
#     def secret(self):
#         self._secrets = []
#     # 这种方法只适用于 getter ，如不希望特性可读，只能使用方法一

# # 什么时候不使用特性？
# # 特性隐藏了赋值时执行的某些计算或处理
# # 当处理过程特别长且复杂，需要异步或并行运行时，会产生问题
# # 必须考虑赋值的与其行为
# # 一些人认为特性应该仅用于弃用曾经公开或已经被完全删除的属性
# # 另一些人认为，对于涉及纯粹的赋值和访问之外的逻辑的getter和setter，特性可作为它们相对简单的替代品
# # 使用前请考虑清楚，特性、公共属性、方法在特定情况下的含义


# --------------------------------------------------------------------------------------------
# # # 特殊方法

# # 也称为魔法方法，允许自定义类添加python运算符/内置命令的支持
# # 特殊方法以双下划线开头和结尾

# # 场景设置
# # 地球经纬坐标

# import math

# class GlobalCoordinates:
#     def __init__(self, *, latitude, longitude):
#         self._lat_deg = latitude[0]
#         self._lat_min = latitude[1]
#         self._lat_sec = latitude[2]
#         self._lat_dir = latitude[3]
#         self._lon_deg = longitude[0]
#         self._lon_min = longitude[1]
#         self._lon_sec = longitude[2]
#         self._lon_dir = longitude[3]

#     @staticmethod
#     def degrees_from_decimal(dec, *, lat: bool = True):
#         if lat:
#             direction = "S" if dec < 0 else "N"
#         else:
#             direction = "W" if dec < 0 else "E"
#         dec = abs(dec)
#         degrees = int(dec)
#         dec -= degrees
#         minutes = int(dec * 60)
#         dec -= minutes / 60
#         seconds = round(dec * 3600, 1)
#         return (degrees, minutes, seconds, direction)

#     @staticmethod
#     def decimal_from_degrees(degrees, minutes, seconds, direction):
#         dec = degrees + minutes / 60 + seconds / 3600
#         if direction == "S" or direction == "W":
#             dec = -dec
#         return round(dec, 6)

#     @property
#     def latitude(self):
#         return self.decimal_from_degrees(
#             self._lat_deg, self._lat_min, self._lat_sec, self._lat_dir
#         )

#     @property
#     def longitude(self):
#         return self.decimal_from_degrees(
#             self._lon_deg, self._lon_min, self._lon_sec, self._lon_dir
#         )

#     # 转换方法
#     # 用大多人希望的方式将对象转化并展示为原始类型，如字符串

#     # 规范字符串 __repr__()
#     # 编写类时虽好定义这个实例方法，返回对象的规范字符串表示，包含对象拥有的所有数据
#     def __repr__(self):
#         return (
#             f"<GlobalCoordinates "
#             f"lat={self._lat_deg}°{self._lat_min}'"
#             f'{self._lat_sec}"{self._lat_dir} '
#             f"lon={self._lon_deg}°{self._lon_min}'"
#             f'{self._lon_sec}"{self._lon_dir}>'
#         )

#     # 易读字符串 __str__()
#     # 与规范字符串类似，但前者更可读、后者调试更有用
#     # 如果没有定义 __str__() ，那么 __repr__() 将被调用
#     def __str__(self):
#         return (
#             f"{self._lat_deg}°{self._lat_min}'"
#             f'{self._lat_sec}"{self._lat_dir} '
#             f"{self._lon_deg}°{self._lon_min}'"
#             f'{self._lon_sec}"{self._lon_dir}'
#         )

#     # 唯一标识符 __hash__()
#     # 哈希值是一个正数，对类实例（即便数据相同）是唯一的
#     # 允许我能在某些集合中使用类实例
#     # 哈希方法应只依赖于实例生命周期内不会改变的值
#     # 如果定义了  __hash__() ，那么官方认为也应该定义  __eq__()
#     def __hash__(self):
#         return hash(
#             (
#                 self._lat_deg,
#                 self._lat_min,
#                 self._lat_sec,
#                 self._lat_dir,
#                 self._lon_deg,
#                 self._lon_min,
#                 self._lon_sec,
#                 self._lon_dir,
#             )
#         )

# nsp = GlobalCoordinates(latitude=(37, 46, 32.6, "N"), longitude=(122, 24, 39.4, "W"))
# print(repr(nsp))
# # <GlobalCoordinates lat=37°46'32.6"N lon=122°24'39.4"W>

# # 将类实例传递给str()，print()，或作为格式化字符串中的表达式时，都会调用__str__()
# print(str(nsp))
# print(nsp)
# print(f"No Starch Press's offices are at {nsp}.")

# print(hash(nsp))
# print(hash(nsp))

# # 其它特殊转换方法
# __bool__() 如果没有定义，检查__len__()是否返回非零值，是则返回True
# __bytes__() 返回一个bytes对象
# __ceil__() 向上取整
# __complex__() 返回复数
# __float__() 返回浮点数
# __floor__() 向下取整
# __format__() 返回应用了格式规范的字符串
# __index__() 无损转换为整数（和__int__相比）
# __int__() 返回整数
# __round__() 四舍五入取整
# __trunc__() 删除非整数部分取整


# # 比较方法
# # 包括==、!=、<、>、<=、>=，返回布尔值
# # 未定义时返回NotImplemented

# # 等于 __eq__()

#     # 表达式self==other将调用self.__eq__(other)
#     # 当然，比较前需要判断other是否为同类型数据
#     def __eq__(self, other):
#         if not isinstance(other, GlobalCoordinates):
#             return NotImplemented
#         return (
#             self._lat_deg == other._lat_deg
#             and self._lat_min == other._lat_min
#             and self._lat_sec == other._lat_sec
#             and self._lat_dir == other._lat_dir
#             and self._lon_deg == other._lon_deg
#             and self._lon_min == other._lon_min
#             and self._lon_sec == other._lon_sec
#             and self._lon_dir == other._lon_dir
#         )

# # 不等于__ne__()
# #     若未定义，则会委托给__eq__()，返回相反值

# # 小于和大于 __lt__()和__gt__()
# #     相互对立的运算符，可相互替换
# #     self<other会调用self.__lt__(other)，如返回NotImplemented
# #     则python会翻转逻辑，调用other.__gt__(self)
# #     因此只定义其中一个即可
# #     代表小于等于和大于等于的__le__()和__ge__()同理

# # 二元运算符支持（接收参数self和other）

# # 减法运算符 -

#     def __sub__(self, other):
#         if not isinstance(other, GlobalCoordinates):
#             return NotImplemented
#         lat_diff = self.latitude - other.latitude
#         lon_diff = self.longitude - other.longitude
#         return (lat_diff, lon_diff)
#     # __rsub__()是__sub__()的反方法，__isub__()对应剑法增强赋值运算符(-=)

# # 13个二元运算符，外加divmod()方法，都依赖于相同的3个特殊方法__x__()、__rx__()、__ix__()
#     # __add__()         加(+)
#     # __sub__()         减(-)
#     # __mul__()         乘(*)
#     # __matmul__()      矩阵相乘(@)
#     # __truediv__()     除(/)
#     # __floordiv__()    向下取整除(//)
#     # __mod__()         求余(%)
#     # __divmod__()      商及余数(divmod())
#     # __pow__()         幂(**)
#     # __lshift__()      左移(<<)
#     # __rshift__()      右移(>>)
#     # __and__()         逻辑与(and)
#     # __or__()          逻辑或(or)
#     # __xor__()         逻辑非(xor)

# # 一元运算符支持（只接受self参数）

# # 取反运算符 ~

#     def __invert__(self):
#         return GlobalCoordinates(
#             latitude = self.degrees_from_decimal(-self.latitude, lat=True),
#             longitude = self.degrees_from_decimal(-self.longitude, lat=False)
#         )

# # 其它一元运算符及其特殊方法
#     # __abs__()         绝对值(abs())
#     # __invert__()      取反/二元翻转(~)
#     # __neg__()         负号(-)
#     # __pos__()         正号(+)

# # 让类可调用的特殊方法 __call__()

# # 可以接收任意数量的参数并返回任何内容

#     def __call__(self, other):
#         EARTH_RADIUS_KM = 6371
#         if not isinstance(other, GlobalCoordinates):
#             return NotImplemented
#         distance_lat = math.radians(other.latitude - self.latitude)
#         distance_lon = math.radians(other.longitude - self.longitude)
#         lat = math.radians(self.latitude)
#         lon = math.radians(self.longitude)
#         a = math.sin(distance_lat / 2) * math.sin(distance_lat / 2) + math.sin(
#             distance_lon
#         ) * math.sin(distance_lon / 2) * math.cos(lat) * math.cos(lon)
#         c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
#         return c * EARTH_RADIUS_KM

# nostarch = GlobalCoordinates(
#     latitude=(37, 46, 32.6, "N"), longitude=(122, 24, 39.4, "W"))
# psf = GlobalCoordinates(
#     latitude=(45, 27, 7.7, "N"), longitude=(122, 47, 30.2, "W"))

# # 相当于nostarch.__call__(psf)
# distance = nostarch(psf)
# print(distance)

# # # 更多特殊方法：
#     # 第九章    可迭代对象的特殊方法
#     # 第十一章  关于上下文管理器的特殊方法
#     # 第十六章  关于异步的特殊方法
#     # 附录A     完整特殊方法的列表


# --------------------------------------------------------------------------------------------
# # # 类装饰器

# # 类支持装饰器，就像支持函数一样，装饰器能封装类的实例化过程
# # 允许添加属性、对包含正在被装饰的类实例的另一个类进行初始化、立即对新对象执行操作等

# class CoffeeOrder:
#     def __init__(self, recipe, to_go=False):
#         self.recipe = recipe
#         self.to_go = to_go

#     def brew(self):
#         vessel = "in a paper cup." if self.to_go else "in a mug."
#         print("Brewing", *self.recipe.parts, vessel)

# class CoffeeRecipe:
#     def __init__(self, parts):
#         self.parts = parts

# special = CoffeeRecipe(["double-shot", "grande", "no-whip", "mocha"])
# order = CoffeeOrder(special, to_go=False)
# order.brew()
# # prints "Brewing double-shot grande no-whip mocha in a mug."

# # 如果不想手动指定每个订单都是外卖订单，
# # 不需要定义一个全新的CoffeeOrder类，只需要定义一个类装饰器
# # 以下是扩展后的代码

# import functools

# class CoffeeOrder:
#     def __init__(self, recipe, to_go=False):
#         self.recipe = recipe
#         self.to_go = to_go
#     def brew(self):
#         vessel = "in a paper cup." if self.to_go else "in a mug."
#         print("Brewing", *self.recipe.parts, vessel)

# class CoffeeRecipe:
#     def __init__(self, parts):
#         self.parts = parts

# def auto_order(to_go):  # 装饰器接收额外参数to_go，因此必须将装饰器封装在另一个函数中
#     def decorator(cls):  # 为此创建一个双重闭包
#         @functools.wraps(cls)
#         def wrapper(*args, **kwargs):
#             recipe = cls(*args, **kwargs)  # 初始化封装类的实例
#             return (
#                 CoffeeOrder(recipe, to_go),
#                 recipe,
#             )  # 用该实例初始化一个CoffeeOrder实例
#             # 然后将CoffeeOrder实例与CoffeeRecipe实例放在一个元组中返回

#         return wrapper

#     return decorator  # 装饰器从最外层函数返回

# @auto_order(to_go=True)
# class CoffeeShackRecipe(CoffeeRecipe):
#     pass

# # CoffeeShackRecipe 继承自 CoffeeRecipe
# # 由于装饰器的存在，实例化 CoffeeShackRecipe 时
# # 实际上一次性实例化了两个对象（通过把它们放在一个元组里）
# # order是一个 CoffeeOrder 类实例，能调用.brew函数
# # recipe是一个 CoffeeRecipe 类实例，它 # 就是 # order.recipe
# order, recipe = CoffeeShackRecipe(["tall", "decaf", "cappuccino"])
# order.brew()
# print(order.recipe is recipe)
# print(f"isinstance(order, CoffeeOrder) = {isinstance(order, CoffeeOrder)}.")
# print(f"isinstance(recipe, CoffeeRecipe) = {isinstance(recipe, CoffeeRecipe)}.")

# --------------------------------------------------------------------------------------------
# # # 对象的结构模式匹配

# --------------------------------------------------------------------------------------------
# # # 函数式编程和面向对象编程

# --------------------------------------------------------------------------------------------
# # # 什么时候使用类？
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
