# 01 快捷键
# 校对
# <Shift+Alt+F>                 Ruff: 自动格式化代码
# <Ctrl+.>                      Ruff: 快速修复建议，Enter执行
# 跳转
# <Alt+UpArrow/DownArrow>       上/下移动整行
# <Shift+Alt+UpArrow/DownArrow> 向上/下复制整行
# 其它
# <ctrl+/>                      切换代码/注释
# <Alt+Shift+A>                 切换代码/注释块
# <Ctrl+D>                      选中下一个相同的词
# 导航
# <Ctrl+P>                      全局搜索文件
# <Ctrl+B>                      打开/隐藏左侧边栏
# <Ctrl+`>                      控制台
#
# 02 虚拟环境venv
# 创建
# <Ctrl+Shift+P>->Python: Create Environment->Venv
# 或命令行：python -m venv .venv
# 会在当前文件夹下创建名为.venv的子文件夹，包含独立的Python解释器和空的库目录
# 激活
# <Ctrl+Shift+P>->Python: Select Interpreter->(.venv)
# 或命令行：.\.venv\Scripts\Activate.ps1
#
# 03 包管理器pip
# 安装(特定版本)的包
# pip install PACK[(==|>=)PACK_VERSION] 
# 更新
# pip install --upgrade PACK
# 卸载
# pip uninstall PACK
# 依赖清单
# pip freeze > requirements.txt
# pip install -r requirements.txt
# pip install --upgrade -r requirements.txt
# 已安装包
# pip list
# 备注
# 完整指令可以在前面加上Python3 -m

# 04 边界清理.gitignore
# 根目录下新建.gitignore文件，无前/后缀
# requirements.txt是必要的
# .gitignore可以：隔离“物理副本” (.venv/)；忽略“缓存” (pycache/)和“配置”(.vscode/)

# 05 启动指南Shebang(Sharp-bang)
# #!/usr/bin/env python3
