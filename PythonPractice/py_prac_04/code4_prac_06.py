
#! (1)
numbers = [1,1]

arraySum = 0    #* 最後とその1つ前の配列の合計値
upperNum = 1000 #* 超過上限

while True:
    if arraySum < upperNum:
        lastNum = len(numbers)-1            #* 最後の配列番号
        theSecondLastNum = len(numbers)-2   #* 最後から1つ前の配列番号
        #? 最後とその1つ前の合計値
        arraySum = numbers[lastNum] + numbers[theSecondLastNum]

        #? 配列に合計値を追加
        numbers.append(arraySum)
    else:
        #? 超過条件を超えた数値の配列を削除し、ループ抜
        numbers.remove(arraySum)
        break
print(numbers)


#! (2)
ratios = list()
count = 0

while count < len(numbers):
    if theSecondLastNum >= 0:
        ratios.append(numbers[lastNum]/numbers[theSecondLastNum])
        lastNum -= 1
        theSecondLastNum -= 1
        count += 1
    else:
        break
print(ratios)

#! (3)
for mult in ratios:
    mult = int(mult * 1000)/1000
    print(mult)
