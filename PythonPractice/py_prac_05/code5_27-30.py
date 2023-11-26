
#! タプルを指定すると面白くなる
def eat(breakfast, lunch = "ラーメン", dinner ="カレー", desserts=()): #* 要素数0のタプルをデフォで指定
    print(f"朝は{breakfast}を食べた")
    print(f"昼は{lunch}を食べた")
    print(f"夜は{dinner}を食べた")

    for d in desserts:
        print(f"おやつに{d}をたべた")

eat("トースト","パスタ","カレー",("アイス","チョコ","パフェ"))

#! タプル部分を可変長引数なるものに変換するとより面白くなる

def eat2(breakfast, lunch, dinner ="カレー", *desserts):
    print(f"朝は{breakfast}を食べた")
    print(f"昼は{lunch}を食べた")
    print(f"夜は{dinner}を食べた")

    for d in desserts:
        print(f"おやつに{d}をたべた")

eat2("トースト","パスタ","カレー","アイス","チョコ","パフェ")
eat2("トースト","パスタ","カレー","アイス","チョコ","パフェ","冬虫夏草","カエンタケ")