
#! 変更不可なリスト = タプル
#? デメリット：変更不可
#? メリット：変更不可ゆえ、中身は安全
scores = (70,80,55)
print(scores)
print(scores[0])

#! 変更するとerror（エラーなのでコメント）
# scores[0] = 77

#! リストで使える関数自体は使用可能
print(f"要素数は{len(scores)}")
print(f"合計は{sum(scores)}")

#! タプルの正体は()の ","
hoge1 = (80)
hoge2 = (80,)
print(type(hoge1)) #* class = str
print(type(hoge2)) #* class = tuple


