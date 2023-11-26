def welcome(u):
    print(f"ようこそ{u["name"]}")
    u["age"] = u["age"] + 1
    print(f"来年{u["age"]}")

userName = "test"
userAge  = 10
user = {"name": userName, "age":userAge}

userCopy = dict(user) #* 防御的コピー
welcome(userCopy)
print(f"{user['age']}歳、{user['name']}")

#! 問題点 -> ageが意図した出力になってない
#! 4行では11、12行では10と表示したい

#? userディクショナリを防御的コピーして使えば解決(10行目)

#* ちなみに、ディクショナリにスライス記法は使えないらしい。使えるのは下記 2つ
#* https://sl.bing.net/fEK5SCIlx1g (>> BingAI)

#* userCopy = user.copy()
#* または
#* userCopy = dict(user)
