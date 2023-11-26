
#! 5-1の最後の問題（閏年を判定する関数）を実際に作ってみろや…　という問題
#* now = datetime.datetime.now()

#! 現在の西暦を宣言
nowYear = 2100

#! うるう年を判定
def isLeapyear(nowYear):
    if nowYear % 400 == 0:
        return True
    elif nowYear % 4 == 0 and nowYear % 100 != 0:
        return True
    else:
        return False

#! 返り値がTrueならうるう年ですと表示する
if isLeapyear(nowYear):
    print(f"西暦{nowYear}年はうるう年です")
else:
    print(f"西暦{nowYear}年はうるう年ではありません")