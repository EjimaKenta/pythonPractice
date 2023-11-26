
#! (1)
temp = [7.8, 9.1, 10.2, 11.0, 12.5, 12.4, 14.3, 13.8, 12.9, 12.4]

#! (2)
for view in temp:
    print(view)

#! (3)
"""print(temp)
temp_new = temp
temp_new[5] = "N/A"
print(temp_new)"""
#? ↑ 横着しすぎてtempとnewTempの中身を同一にしてしまった反省

temp_new = list()
for count in range(len(temp)):
    if count == 5:
        temp_new.append("N/A")
    else:
        temp_new.append(temp[count])
print(temp)
print(temp_new)

#! (4)
tempSum=0           #* 合計格納

for avg in temp_new:
    #* 計測不可は計算しない
    if not isinstance(avg,float):
        continue
    tempSum += avg
 
#! 計算不可を換算しないVer
print(tempSum/(len(temp_new) - 1))
