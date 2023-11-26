
#! デフォルト関数 -> def 関数名(引数1="デフォルト値", …)
def eat(breakfast, lunch, dinner = ""):
    print(f"朝は{breakfast}を食べました。")
    print(f"昼は{lunch}を食べました。")
    print(f"夜は{dinner}を食べました。")

print("8/1")
eat("トースト","おにぎり","カレー")

print("8/2")
eat("納豆ご飯","ラーメン","カレー")

print("8/3")
eat("バナナ","そば")

print("8/4")
eat("サンドウィッチ","シュウマイ弁当","カレー")
