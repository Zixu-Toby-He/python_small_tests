import pathlib

当前路径 = pathlib.Path(".")

def 路径遍历(根目录, 路径回调函数):
	for i in 根目录.iterdir():
		路径回调函数(i)
		if i.is_dir():
			if (not(i.is_symlink())):
				# 符号链接不参与遍历
				路径遍历(i, 路径回调函数)
		else:
			pass

def 测试回调函数(文件路径):
	print(文件路径)


路径遍历(当前路径, 路径回调函数 = 测试回调函数)

