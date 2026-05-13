# import pathlib
from pathlib import Path

# 路径获取

# # Construct a PurePath from one or several strings and or existing PurePath objects.
# # The strings and path objects are combined so as to yield a canonicalized path,
# # which is incorporated into the new PurePath object.
# my_path = Path("./test1.txt")
# print(f"path: {my_path}, type: {type(my_path)}")
# # path: test1.txt, type: <class 'pathlib.WindowsPath'>

# # Return a new path pointing to the user's home directory
my_home_directory = Path.home()
# print(f"home: {my_home_directory}, type: {type(my_home_directory)}")
# # home: C:\Users\53596, type: <class 'pathlib.WindowsPath'>

# # Return a new path pointing to the current working directory.
my_current_working_directory = Path.cwd()
# print(f"cwd: {my_current_working_directory}, type: {type(my_current_working_directory)}")
# # cwd: C:\Users\53596\python\capri, type: <class 'pathlib.WindowsPath'>

# # 路径拼接
path_part0 = Path("/user")
path_part1 = Path("/downloads")
path_full = path_part0 / path_part1 / "music" / "jazz"
# print(f"path_full: {path_full}")
# # path_full: \downloads\music\jazz

# # 文件属性
file_path = my_current_working_directory / "lib_learning/std_pathlib/test1.txt"
file_basename = file_path.name
file_stem = file_path.stem
file_suffix = file_path.suffix
file_parent = file_path.parent
# print(
#     f"path: {file_path}\nname: {file_basename}\nstem: {file_stem}\nsuffix: {file_suffix}\nparent: {file_parent}"
# )
# # path: C:\Users\53596\python\capri\lib_learning\std_pathlib\test.txt
# # fullname: test.txt
# # stem: test
# # suffix: .txt
# # parent: C:\Users\53596\python\capri\lib_learning\std_pathlib


# # 路径/文件判断
def is_exsists(path: Path):
    if path.exists():
        print(f"The path does exist: {path}")
    else:
        print(f"The path doesn't exist: {path}")
test_path_rel = Path("./test1.txt")
is_exsists(test_path_rel)
test_path_rel = Path("./lib_learning/std_pathlib/test1.txt")
is_exsists(test_path_rel)
test_path_abs = my_current_working_directory / "lib_learning/std_pathlib/test1.txt"
is_exsists(test_path_abs)
print(Path.is_file(my_current_working_directory))
print(Path.is_file(test_path_rel))

# # 创建目录 Path.mkdir()
# try:
#     Path("tempfile/tempfile1").mkdir()
# except FileNotFoundError:
#     print("File not found!")
# except FileExistsError:
#     print("File exists!")

# Path("temp_dir/temp_dir2").mkdir(parents=True, exist_ok=True)
# parents=True 能递归创建目录，防止 FileNotFoundError
# exist_ok=True 能防止目录已存在的异常 FileExistsError

# # 创建文件 Path.touch()
test_path = Path("temp_dir/temp_dir2/temp_file.txt")
test_path.parent.mkdir(parents=True, exist_ok=True)
test_path.touch(exist_ok=True)
# # 要确保路径是存在的，touch() 只能新建文件，路径不存在引发异常 FileNotFoundError

# # 重命名 Path.rename()

new_path = test_path.with_name("temp_file2.txt")
# Path.with_name(self, arg)返回实例完整路径，只改变文件名为 "arg"
# # 类似的，with_系列还有很多函数，可以只改变前缀、后缀等
# # 把返回值赋予给新变量名称 new_path

test_path = Path.rename(test_path, new_path)
# # Path.rename(self, arg)用于重命名，如果新名称已存在会报错
# # 等价于 test_path.rename(new_path)
# Path.replace(test_path, new_path)
# # Path.replace(self, arg)用于重命名，如果新名称已存在会覆盖
# # 两个重命名函数都会返回新的 Path 值，将其绑定到 test_path ，完成路径更新！

