def trans(字符串, 编码格式 = "utf-8"):
	编码字符串 = repr(字符串.encode(编码格式))[2:-1]
	分割	  = 编码字符串.split("\\")
	for i,j in enumerate(分割):
		if (len(j) == 0):
			# 不转化
			pass
		elif (j[0] == "x"):
			分割[i] = "x" + j[1:].upper()
		else:
			# 不转化
			pass
	编码字符串 = "\"{}\"".format("\\".join(分割))
	return 编码字符串

# 测试
编码格式 = input("请输入编码格式：")
字符串   = input("请输入需要转化的字符串：\n\t")
print(trans(字符串))
