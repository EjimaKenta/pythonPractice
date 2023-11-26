userinfo = input("名前と血液型をカンマで区切って一行で入力>> ")
[name, blood] = userinfo.split(",")
blood = blood.upper().strip()
print(f"{name}さんは{blood}型なので大吉です。")

#* split -> ""内の文字を基準に文字列を分割し、リストで返す
#* upper -> 英字を大文字にする
#* strip -> 文字列前後の空白を取り除く