
#! クラス宣言
class Hero:
    #! 追記：コンストラクタについて
    #? コンストラクタが有る場合は、フィールド変数は不要
    #? def __init__(self, name="松田", hp=32): デフォルト関数指定も可能。その場合はクラスを空(h=Hero() -> 松田,32)で発行可
    def __init__(self, name, hp): #* これがコンストラクタになる (init → initialized：初期化)
        self.name = name
        self.hp  = hp

    #? クラス内のメソッドの第一引数は「お約束」で絶対書く。自身を表すオブジェクトになる。
    def sleep (self, hours):
        print(f"{self.name}は{hours}時間寝た")
        self.hp += hours

#!ゲーム開始
print("スッキリファンタジーⅫ ~金色の理想郷~")
#// h = Hero()
h = Hero("松田",32)
h.sleep(3)
print(f"{h.name}のHPは現在{h.hp}です")
