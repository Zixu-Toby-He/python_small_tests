import os

包名   = input("请输入包名称：")
返回值 = os.system("pip install {} -i https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple".format(包名))
print()
print()
print()
if (返回值):
	print("下载失败")
else:
	print("下载成功")
print()
print()
print()
os.system("pause")