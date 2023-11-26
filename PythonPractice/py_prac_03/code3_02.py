name = input ("あなたの名前を教えてください>> ")

print (f"{name}さん、こんにちわ")
food = input(f"さんの好きな食べものを教えてください>> ")

#! インデントを指定通りにしないとエラー（print 及び else）
#? インデントが各ブロックを指定(表現)しているとのこと
if food == "カレー":
    print("素敵です。カレーisBest")
else:
    print(f"私も{food}が好きですよ")

