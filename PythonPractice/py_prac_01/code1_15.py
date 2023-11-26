"""
#! これはエラーが出る
#?（データ型がstrとstrで計算しようとしてサポ外(unsupported)と弾かれている
price = input("料金を入力 >>")
num = input("人数を入力 >>")

payment = price // num
print("お支払いは",payment,"円です。")
"""

#* 正しいのは下記 P71~2_コード1-22
price = int(input("料金を入力 >>"))
num = int(input("人数を入力 >>"))

payment = price // num
#? print("お支払いは",payment,"円です。")
#? フォーマット関数を使うとこのような簡便な書き方も可能
print(f"お支払いは{payment}円です。")