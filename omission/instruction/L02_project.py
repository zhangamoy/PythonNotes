#!/usr/bin/env python

# --------------------------------------------------------------------------------------------
# # # 版本管理系统 Git

# # install: winget install --id Git.Git -e --source winget
# # 项目仓库下应该有README.md、LICENSE.md、.gitignore、[Folder: {Project}]
# # python代码应放在单独子目录中
# # module(模块)就是一个.py文件
# # package(包)就是包含一个或多个module的目录
# # 该目录必须包含__init__.py，否则python不知道相应目录会构成一个package
# # 项目结构中，最高一级文件夹称为顶级包，下一级为它的子包
# # 文件名应小写+下划线分隔，目录名应小写尽量不用下划线

# # # 项目结构

# # omission-git/
# # |--- LICENCE.md
# # |--- omission/  # 顶级包
# # |   |--- __init__.py  # 顶级包的标志
# # |   |--- __main__.py  # 顶级包下的特殊文件，用命令 python -m omission来运行(python __main__.py可以吗)
# # |   |--- app.py
# # |   |--- common/  # 子包
# # |   |   |--- __init__.py  # 子包的标志
# # |   |   |--- classproperty.py
# # |   |   |--- constants.py
# # |   |   |--- game_enums.py
# # |   |--- data/
# # |   |   |--- __init__.py
# # |   |   |--- data_loader.py
# # |   |   |--- game_round_settings.py
# # |   |   |--- scoreboard.py
# # |   |   |--- settings.py
# # |   |--- interface/  # 不是常规的包
# # |   |--- game/
# # |   |   |--- __init__.py
# # |   |   |--- content_loader.py
# # |   |   |--- game_item.py
# # |   |   |--- game_round.py
# # |   |   |--- timer.py
# # |   |--- resources/
# # |   |--- tests/
# # |   |   |--- __init__.py
# # |   |   |--- test_game_item.py
# # |   |   |--- test_game_round_settings.py
# # |   |   |--- test_scoreboard.py
# # |   |   |--- test_settings.py
# # |   |   |--- test_test.py
# # |   |   |--- test_timer.py
# # |--- omission.py
# # |--- pylintrc
# # |--- README.md
# # |--- .gitignore

# --------------------------------------------------------------------------------------------
# # # 导入模块和函数

# # 导入模块（模块化引用）
# # 导入一个模块L99_附录.py，并调用其中的函数
# import L99_appendix
# # "L99_附录"是函数"open()"的命名空间，即，对某些对象(如函数)的显式定义路径
# L99_appendix.open()
# L99_appendix.close()

# # 导入函数（显式导入）
# from L99_appendix import open as door_open, close as door_close
# door_open()
# door_close()
# syntax: from module import fn[, fn2]
# 可以在不添加命名空间的情况下调用函数
# syntax: from module import fn[ as fn_new]
# 重命名函数防止覆盖

# # 导入所有（隐式导入）
# from L99_appendix import *
# open()
# # 警告：`from L99_appendix import *` used; unable to detect undefined names
# # 解释：通配符导入 (import *) 破坏了代码的静态可寻址性（static addressability）
#     # 当写 from L99_appendix import * 时：
#     # 静态失效：Ruff 不运行代码，不知道 L99_appendix 里面到底有 10 个变量还是 100 个变量
#     # 寻址断裂：当下一行写 open() 时，工具查遍了你当前文件的定义，没找到 open，又无法确定 my_value 是否在L99_appendix里面
#     # 后果：工具失去了对代码的“监控权”，如果拼写错误，工具也无法提示
# # 建议：在底层开发中，明确的引用链（Explicit Reference）比隐含的便捷（Implicit Convenience）更安全

# --------------------------------------------------------------------------------------------
# # # 包的嵌套

# # 绝对导入（起点取决于搜索路径 sys.path）
# from omission.temp import test
# test()
# # 报错：ModuleNotFoundError
# # 解释：#F5#运行 L02_project_structure.py 时，解释器会自动将该文件所在的直接目录加入搜索路径的第一位sys.path[0]
#     # 解释器的寻址起点 sys.path[0] 就在 instruction/ 内部
#     # 解释器在 instruction/ 文件夹里找一个名为 omission 的子文件夹，没找到（实际它是父级文件夹）
# # 方案：工程根目录（即 omission 文件夹的上一层）启动程序
#     # 在终端（Terminal）中使用 cd 命令退回到项目的根目录，使用 -m 参数（模块化运行方式）来启动：
#     # python -m omission.instruction.L02_project_structure

# # 相对导入（起点取决于身份设定）
# from ..temp import test
# test()
# # 相当于绝对导入的
# # from omission.temp import test
# # 其中，..temp == omission.temp (上级目录)
# # 类似的， .temp == instruction.temp (当前目录)
# # 还可以用 "..." 代表上两级目录

# # 两种运行方式/两种导入方式的对比
#     # 运行方式  直接运行 / F5 / python *.py    模块化运行 / python -m pkg.*
#     # 搜索路径  所在包文件夹(instruction)      工程根目录 omission 的上一层(CAPRI)
#     # 绝对导入  只能导入instruction内的模块     可导入所有omission下的所有模块
#     # 身份设定  且当前模块自认为顶层模块        视自己为包的一部分
#     # 相对导入  不可用，因为找不到父包          可用
# # 物理位置≠逻辑身份——直接运行是自立为王，模块运行是归入版图
# import sys
# print(sys.path[0])
# # 直接运行：C:\Users\53596\python\capri\omission\instruction
# # 模块化运行：C:\Users\53596\python

# --------------------------------------------------------------------------------------------
# # # 入口点

# # 模块入口点 __name__=="__main__"
# import omission.temp
# import omission.instruction.temp as ins_temp
# print(__name__) # __main__
# print(omission.temp.__name__) # omission.temp
# print(ins_temp.__name__) # omission.instruction.temp
# # __name__ 通常为模块的完全限定名称，即从sys.path[0]开始的完整路径
# # 除非当一个模块或包被直接运行时，__name__ 设定值为  __main__
# if __name__ == "__main__":
#     print("We're in the module entry.")
# # 直接执行模块时才运行的语句，可以先进行条件判断

# # 包入口点 __main__.py
# # 情况1  命令python -m omission，相当于运行包内的__init__.py和__main__.py
# # 情况2  如果import omission，则只运行__init__.py
# # 情况3  如果没有__main__.py，包将不能被直接执行
# # 在__main__.py中：
# # def main():
# #     print("Go!")
# # if __name__ == "__main__":
# #     main()
# import omission.__main__  # 不会打印"Go!"
# # 在__main__.py中改成：
# # def main():
# #     print("Go!")
# # main()
# # 即便__main__被导入，也会打印"Go!"

# # 控制包的导入 __init__.py
# # 用途1：简化导入，
# # 在 __init__.py中：
# # from .temp import test
# # 诸如此类地，这样我们可以直接从顶级包导入函数/类，省略了中间的路径
# # from omission import test
# # test()
# # 用途2：控制"导入所有"(import *)的行为
# # 在 __init__.py中：
# # from .temp import test
# # from .temp import test2
# # from .temp import test3
# # from .instruction.temp import ins_test
# # __all__ = ["test", "test2", "test3", "ins_test"]
# # 于是我们可以快速导入顶级包 omission 中四个函数
# from omission import *
# test()
# test2()
# test3()
# ins_test()

# # 程序入口点
# # 在顶层包 omission 外部建立模块 run_omission.py:
# # from omission.__main__ import main
# # main()
# # 于是执行 omission 包 python -m omission
# # 就等价于
# # 执行.py文件 python run_omission.py
# from omission.__main__ import main
# main()
# main()
# # 特别注意，python run_omission.py中.py是必要的，否则run_omission将会被视为一个包
# # 此外这个run_omission.py是非必要的，只是提供了快捷方式
# # 如果像教材那样设定为同名omission.py，则很容易因为重名导致"同名遮蔽"
# # 另外，把.py放在顶层包之外，就是方便直接运行脚本
# # 放在本L02_project_structure.py中也不是不行，只不过必须模块化运行，否则import失败

# --------------------------------------------------------------------------------------------
# # # 模块搜索路径 sys.path

# # 模块搜索路径是一个list[str]，导入系统按它指定的顺序搜索模块
# import sys
# print(sys.path)
# # 一般的顺序是：当前运行脚本的目录(不是工程的根目录)，python标准库，虚拟环境中用pip安装的内容
# # ['C:\\Users\\53596\\python\\capri\\omission\\instruction', 
# # 'C:\\Program Files\\RevvitySignalsSoftware\\ChemDrawApplications\\ChemScript\\Lib', 
# # 'C:\\Program Files (x86)\\CambridgeSoft\\ChemOffice2014\\ChemScript\\Lib', 
# # 'C:\\Program Files\\Python39\\python39.zip', 
# # 'C:\\Program Files\\Python39\\DLLs', 
# # 'C:\\Program Files\\Python39\\lib', 
# # 'C:\\Program Files\\Python39', 
# # 'c:\\Users\\53596\\python\\capri\\.venv', 
# # 'c:\\Users\\53596\\python\\capri\\.venv\\lib\\site-packages']
# # 如果需要在模块搜索路径中添加位置，最好使用虚拟环境
# # 并在 lib/python3.x/sitepackages目录中添加以.pth结尾的任意名文件
#     # venv/lib/python3.10/site-packages/stuff.pth
#     # 绝对路径
#     # /home/jason/bunch_of_code
#     # 相对路径(相对于.pth，指向venv/中的awesomesauce)
#     # ../../../awesomesauce

# --------------------------------------------------------------------------------------------
# # # 导入系统

# # 导入语句会调用内置的__import__()函数
# # 如果想手动执行导入，请使用importlib模块，而不是直接调用__import__()
# # 导入模块需要两个特殊对象：查找器和加载器

# # 查找器
# # 元路径查找器(meta path finder)，存放在sys.meta_path列表中，默认包括
#     # 内置模块导入器(built-in importer)：寻找sys、time等直接集成在python解释器中的模块
#     # 冻结模块导入器(frozen importer)：寻找被冻结在可执行文件中的字节码模块
#     # 基于路径的查找器(path-based finder)：遍历sys.path，寻找本地编写的模块或安装的第三方包
# # 内置模块是用C/C++编写的（为了性能），相当于python的硬件
# # 冻结模块是用python编写的（为了实现），相当于python预装在芯片中的软件，用于管理其它软件的加载
# # 内置和冻结模块都在python解释器启动时完成加载
# # 但这不意味着它们对我们是可见的，import还是必要的
#     # 注：importlib
#     # Python 的整个导入逻辑是用 Python 编写的（即 importlib）
#     # 但为了能让 Python 具备“导入”的能力，它必须在没有文件系统支持的情况下先把自己导入
#     # 因此，importlib 的核心部分被冻结在解释器中，由冻结模块查找器负责加载
# # 查看冻结模块的代码如下
# import _frozen_importlib
# import sys
# frozen_modules = [m for m in sys.modules if getattr(sys.modules[m], "__loader__", None) == _frozen_importlib.FrozenImporter]
# print(frozen_modules)
# # 除了默认的查找器，还可以自定义新的查找器放入sys.meta_path中
#     # 从网络导入
#     # 从数据库导入
#     # 加密加载

# # 加载器
# # 创建：加载器根据模块规范，创建空的模块对象
# # 预注册：把对象添加到sys.modules中（防止循环引用）
# # 加载：获取源码→编译成字节码（尝试缓存.pyc，放在__pycache__文件夹中）
# # 执行：在模块的命名空间内执行代码（函数和类被创建）
# # 属性填充：设置__name__等元数据
# # 名称绑定：import 将该对象赋值给本地变量
# # 注：为了确保不加载过时的缓存，可以对比时间戳或者哈希值
# # 查看__name__属性的代码如下
# import math as m
# n=m.acos
# print(m.__name__)
# print(n.__name__)
