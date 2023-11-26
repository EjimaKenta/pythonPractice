
#! in演算子はリスト型の中に対して比較をかけれる
score = [80,100,20,60]
if 100 in score:
    print("満点あるやん賞")
else:
    print("教育教育死刑賞")

#! 3-6も追記しちゃう。ディクショナリ型に対しても比較をかけれる
scores = {"network":60, "database":80, "security":50}

key = input("追加科目名を入力")
if key in scores:
    print("既登")
else:
    data = int(input("得点を入力してください>> "))
    scores[key] = data
print(scores)