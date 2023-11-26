
"""#! 入力ターム
japanese_sbj = input("国語の点数を入れろ")
arithmetic_sbj = input("算数の点数を入れろよ！")
science_sbj = input("理科の点数を入れろぉお！")
social_sbj = input("社会の点数を入れろって！")
english_sbj = input("英語の点数を入れてよぉ！")

#! 配列宣言
subjects = [
    int(japanese_sbj),
    int(arithmetic_sbj),
    int(science_sbj),
    int(social_sbj),
    int(english_sbj)
]

#! 計算ターム
print(f"合計点:{sum(subjects)}")
print(f"平均点:{sum(subjects)/len(subjects)}")
"""

#! 模範解答（こっちのほうが頭いい）
#? appendで追加をちゃんと活用しよう………………………
scores = []
scores.append(int(input("国語の点数>>")))
scores.append(int(input("算数の点数>>")))
scores.append(int(input("社会の点数>>")))
scores.append(int(input("理科の点数>>")))
scores.append(int(input("英語の点数>>")))

#! 計算ターム
print(f"合計点:{sum(scores)}")
print(f"平均点:{sum(scores)/len(scores)}")