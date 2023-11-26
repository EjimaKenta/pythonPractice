import random

#! 桁数変数 及び 各リスト定義
endFlag = True              #* クリアフラグ
digit = 3                   #? 桁数変更
answer = [0] * digit        #* 正解リスト
prediction = [0] * digit    #* 回答リスト

while endFlag:
    print("数当てゲーム、3桁の数字を当てろ")

    #! 指定桁数分の乱数をリスト格納
    for i in range(digit):
        answer[i] = random.randrange(10)
        if not (answer[i] in answer):
            i -= 1

    print(answer)#* リスト表示デバック

    #! ユーザー回答をリスト格納
    for i in range(digit):
        prediction[i] = int(input(f"{i+1}桁の予想を入力(0~9)>> "))
    print(prediction) #* リスト表示デバック

    hitCount  = 0
    ballCount = 0

    #! Hit&ballチェック
    for i in range(digit):
        if answer[i] == prediction[i]:
            hitCount += 1
        if prediction[i] in answer:
            ballCount += 1
    ballCount -= hitCount

    #! 結果発表
    print(f"{hitCount}ヒット！{ballCount}ボール！")

    #! コンティニュー伺い
    if hitCount == digit:
        print("正解です")
        endFlag = False
    else:
        continueGame = int(input("続けますか？1:y 2:n >> "))
        if continueGame == 2:
            print(f"正解は{answer}でした")
            endFlag = False
