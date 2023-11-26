
#! 各関数について、定義の一行目に記述する内容と、戻り地がある場合は、望ましいデータ型を答えてください。
#! なおデータ型は、表1-6(P061)の4つ（str, int, float, bool）か、リスト, ディクショナリ, タプル, セット から選ぶものとする

#! (1) 戻り値不要
#? 戻り地不要
def weather():
    print("今日は晴れです")

weather()

#! (2) 戻り値必要 , float型
radius = 5
def calc_circle_area(radius):
    print(radius*radius*3.14)

calc_circle_area(radius)

#! (3) 戻り値必要 , str型
import datetime

def nowstr():
    now = datetime.datetime.now()
    return f"{now.hour}時{now.minute}分{now.second}秒"

print(nowstr())

#! (4) 戻り値必要 , list型
def nowint():
    now = datetime.datetime.now()
    nowList =[now.hour, now.minute, now.second]
    return nowList

print(nowint())

#! (5) 戻り値必要 , bool型
nowYear = 2104
def isLeapyear(nowYear):
    if nowYear % 400 == 0:
        return True
    elif nowYear % 4 == 0 and nowYear % 100 != 0:
        return True
    else:
        return False

print(isLeapyear(nowYear))
#! 2000年 → TrueでOK、2100年 → False でOK、2104年 → True でOK。s