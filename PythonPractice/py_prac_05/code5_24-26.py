
#! 引数キーワード指定 -> 関数名(実引数1 = "〇〇", 実引数2 …)

def eat(breakfast, lunch = "ラーメン", dinner ="カレー"):
    print(f"朝は{breakfast}を食べた")
    print(f"昼は{lunch}を食べた")
    print(f"夜は{dinner}を食べた")

#? 関数呼び出し時に渡す実引数に実数を入れる
eat("満漢全席",lunch="カレイの煮つけ") #* デフォランチはラーメンだが、呼び出し時にランチの内容を指定して変更可



