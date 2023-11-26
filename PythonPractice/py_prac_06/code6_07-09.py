
#! identity の確認
score1 = [80, 40, 50]
score2 = [80, 40, 50]
print(f"score1の先頭要素:{score1[0]}")
print(f"score2の先頭要素:{score2[0]}")

print("変数s2の中身を変数s1に代入する")
score1 = score2

print("s1の先頭要素を90に書き換え")
score1[0] = 90

print(f"90を代入したs1の先頭要素は{score1[0]}")
print(f"90を代入していいないs2の先頭要素は{score2[0]}")

#! 関数と参照渡しの組み合わせの罠
def add_suffix(names):
    for i in range(len(names)):
        names[i] = names[i] + "さん"
    return names

before_names = ["松田","浅木","工藤"]
    #? >>>>> 防御的コピーについて(6-9)
copied_names = list()
for n in before_names:
    copied_names.append(n)
    #? <<<<<

after_names = add_suffix(copied_names)
after_names = add_suffix(before_names)
print("さん付けあと:" + after_names[0])
print("さん付けまえ:" + before_names[0])
print("防御的コピー:" + copied_names[0])
