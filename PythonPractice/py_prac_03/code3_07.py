score = int(input("試験点数を書く"))
country   = input("ってかどこ住み？ｗ")

#? 60以上でTrue 以下でFalse
print(score >= 60)

#? 60以上 かつ 100以下 (and)
print(60 >= score and score <= 100)
#! pythonだけできる記法
print(60 >= score <= 100) #* 60以上、100以下

#? 60未満 または 100以上 (or)
print(60 < score or score > 100)

#? 60以上 または 100以下 (not)
print(not(60 < score or score > 100))

#? score に 6 が含まれる (in)
if "県" in country:
    print("県住みマン")

#? score に 6 が含まれない (not-in)
if not "県" in country:
    print("ノー県住みマン")