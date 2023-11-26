text = input("何記録奴？>> ")

#! 教科書にはencoding文が無いが、無いと文字化けするので追記すること
file = open("diary.txt", "a",encoding="UTF-8")
file.write(text + "\n")

#! closeしないと別で操作する際に使用中として断られる可能性がある
file.close()