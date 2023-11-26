
#! (1)
isError = False
n = 10

if isError == False and n < 100:
    print("ぬわ")

#! (2)
inNum = int(input("num >>"))
if inNum%2 == 0:
    print("偶")
else:
    print("奇")

#! (3)
inStr = input("なんか言え>> ")
if inStr == "こんにちは":
    print("ようこそ")
elif inStr == "景気は？":
    print("ぼちぼち")
elif inStr == "さようなら":
    print("お元気で！")
else:
    print("どうした？")

#! (4)
#? block1 => 1,3,5,7,8,10,12
    #* '31日までありますね'     // 〇ヶ月過ぎました
#? block2 => 4,6,9,11
    #* '30日までですね'         // 年が明けてから〇ヶ月過ぎました
#? block3 => 2
    #* '1年で一番寒い月ですね'  // 年が明けてから〇ヶ月過ぎました。