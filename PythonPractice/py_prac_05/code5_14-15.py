def plus(x, y):
    answer = x + y
    return answer

answer = plus(100, 50)
print(f"足し算の答えは{answer}です")


#! 関数を変数に代入することも可能らしい
answer = plus
print(answer(10,20)) #? answer関数に本来Puls関数に使う引数を入れても成立するようになる

#! 例題では3つ関数を用意し、リストに格納。ランダム関数でリスト番号をランダムに出力し結果を表示させてた
#? list = [def1, def2, def3]
#? list[rand関数(0, 2)]() -> def1~3のいずれかが出力する。
#? ゲームでランダム実行が起こり得る際には有効とのこと
