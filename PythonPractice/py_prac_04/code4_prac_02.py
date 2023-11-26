
#! (1) ~ (6)を順次記載してWhileループ文を作れ的な問題
count = 0
while True:
    print("カレーを召し上がれ")
    print(f"{count}皿のカレーを食べました")
    refilles = input("おかわりはいかが？(y/n)>> ")
    if refilles == "y":
        count += 1
    else:
        print("ごちそうさまでした。")
        break