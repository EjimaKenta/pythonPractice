
#! よくわからん仕様
#? 値渡しと参照渡し

#? 値渡し
#* numが渡されているけど、関数に渡される引数は元の引数のコピーなので、
#* 関数内で色々やっても元には影響を与えない。
#* 関数外のオリジナルに影響させたいときはreturn文を使って再代入しよう
num = 5
def addNum(num):
    num += 5
    print(f"デフフ… こっちはaddNum内の{num}")

addNum(num)
print(f"こっちは普通の{num}")
print("おや、増えてないよ")
print("")


#? 参照渡し
scores = [1,2,3]
def addScoresZeroNum(scores):
    scores[0] += 5
    print(f"デフフ… こっちはaddScoresZeroNum内の{scores}")

addScoresZeroNum(scores)
print(f"こっちは普通の{scores}")
print("おや、5増えてるよ")
