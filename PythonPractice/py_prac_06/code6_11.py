
#! リストの場合
names = list()
print(f"変更前のlistのidentity:{id(names)}")
names.append("松田")
print(f"変更前のlistのidentity:{id(names)}")

#! 文字列の場合
name = "松田"
print(f"変更前のstrのidentity:{id(name)}")
name = "スーパー" + name
print(f"変更前のstrのidentity:{id(name)}")

