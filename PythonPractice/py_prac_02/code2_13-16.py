
#! ディクショナリ通常利用
scores = {"network":60,"database":80,"security":50}
print(scores)

#! ディクショナリ要素指定
print(scores["network"])

#! ディクショナリ要素追加
scores["security"] = 55
scores["programming"] = 65  #? 最終行に追加

print(scores)

#! ディクショナリ要素の削除（del文）
del scores["security"]
print(scores)

#! ディクショナリにも pop関数 が存在する
    #? remove関数は存在しない
    #? popされたディクショナリは消失(以降のprintで出現しなかった)
print(scores.pop("network"))    #*pop内にはディクショナリ名を指定 -> 要素数ではない

#! 一部中身のみ確認可能な関数が存在する (関数を使うと型が変わる)
#* 参考文書: https://www.self-study-blog.com/dokugaku/python-dict-method-keys-values-items-get-setdefault/
print(scores.keys())    #? キーのみ出力。型は dict_keysオブジェクト
print(scores.values())  #? 値のみ出力。型は dict_valuesオブジェクト
print(scores.items())   #? 全体を出力。型は dict_itemsオブジェクト

#* values関数を用いた使用例
print(sum(scores.values()))