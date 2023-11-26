# 趣味は任意：https://sl.bing.net/jq61RLlKhxI

#! (1)一人目の趣味設定
A_hobbies = {"量子コンピューティング", "ブラックホール探索", "宇宙塵収集", "テレポーテーション"}

#! (2)二人目の趣味設定
B_hobbies = { "マルチバース探検", "ブラックホール探索", "テレポーテーション", "宇宙塵収集", "星間旅行", "ダークマター研究"}

#! (3)略
#* Enter待ち
input("心の準備ができたらEnterキーを押してください")

#! (4)略
union_AB = A_hobbies | B_hobbies            #* 和集
intersection_set_AB = A_hobbies & B_hobbies #* 積集

#? 数値化
uniNum    = len(union_AB)
intsecNum = len(intersection_set_AB)

#? 相性度計算
compatibility = intsecNum/uniNum *100

print(f"AとBの相性度は「{int(compatibility)}%」！！！！！")