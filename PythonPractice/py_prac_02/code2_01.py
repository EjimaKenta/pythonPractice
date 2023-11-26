network = 88
database = 95
security = 90
total = network + database + security
avg = total / 3 #!素の数字 -> マジックナンバー -> 変更の工数がかかるので極力使わない
print(f"合計点:{total}")
print(f"平均点:{avg}")