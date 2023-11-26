scores = [80,20,75,60]

#! while文(4-6 P 169)
count = 0

while count < len(scores):
    if scores[count] >= 60:
        print("合格")
    else:
        print("不合格")
    count += 1
print("")

#! for文_デフォで拡張For文っぽい(4-7 P171)
#? より Elegantで Betterな CodeWritingさ Baby…
for data in scores:
    if data >= 60:
        print("合格")
    else:
        print("不合格")
print("")

#! 通常for文に近いfor文の記述(4-8 P174)
for num in range(3):
    print("Python楽しい")
print(list(range(1,3)))
