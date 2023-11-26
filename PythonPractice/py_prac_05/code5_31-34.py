
name = "松田"
def hello():
    print("こんちわ"+name+"さん")

name2 = "松田"
def change_name():
    name2 = "浅木" #* ここでname2を松田から浅木にしようとするも敗北…

def hello():
    print("こんにちは"+ name2 + "さん")

change_name()
hello()

#! グローバル変数の指定
name3 = "松田"
def change_name():
    global name3
    name3 = "浅木"

def hello():
    print("こんにちは"+ name3 + "さん")

change_name()
hello()

#! グローバル変数は色々自由すぎるし他の様々な関数をぶち殺してしまうかも知れないので、
#! 乱用せずにきちんと関数やらを組み合わせて安全なプログラムを作ろう。