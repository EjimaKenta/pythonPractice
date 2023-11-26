
#! セットのルール
#? 順不同（添字も存在しない）
#? 順不同のため、特定の要素を指定した操作は不可
#? 要素の重複不可
#? 要素追加には add関数 を使用(appendは不可)

#! セットの利用
scores = {70,80,55,80}
scores.add(80);

print(scores)   #* デフォ80重複のため、3要素のみ。addも無効。
print(f"要素数は{len(scores)}")
print(f"合計は{sum(scores)}")
