members = ["松田","工藤","浅木"]
members.remove("浅木")
del members[1]          #!要素数で指定可能
mems = members.pop(0)   #! popは戻り値が返ってくることが特徴
print(members)
print(mems)
