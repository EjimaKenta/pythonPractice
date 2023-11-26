
#! walk(); take_bus(); run(); run()
#! 上記のようにメソッドを走らせる際に、run()で走ったら必ず歩きを入れるように修正せよとのこと
"""
def take_bus():
    print("バス乗")

def run():
    print("走")

def walk():
    print("歩")
"""

#! run()メソッド内に walk() を入れてあげれば良い。
#! 関数巻取りが無いからwalk()をrun()より上に配置する
#? なお試したが、run()上でも動く模様。ここだけよくわからん。
def take_bus():
    print("バス乗")

def walk():
    print("歩")

def run():
    print("走")
    walk()

walk(); take_bus(); run(); run()