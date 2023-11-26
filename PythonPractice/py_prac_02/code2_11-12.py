nums = [10,20,30,40,50]
print(nums[1:3])    #? 添字が1以上3未満 （1,2番目を表示）
print(nums[2:])     #? 添字が2以上の全て（2,3,4番目を表示）
print(nums[:3])     #? 添字が3未満の全て（0,1,2番目を表示）

#! 負の数を利用したスライス構文
    #* 正の数で見る要素順 = [ [0], [1], [2], [3], [4]]
    #? 負の数で見る要素順 = [[-5],[-4],[-3],[-2],[-1]]

print(nums[-1])     #? 末尾の要素を参照
print(nums[-2])     #? 末尾から2番めの要素を参照
print(nums[-5:-2])  #? 負の数でスライス利用も可能（0番以上4未満_10,20,30）

#! スライスを利用した要素のねじ込み
nums[2:3] = [44]    #? スライスで挿入する場合、挿入する内容に[]を付ける
print(nums)

#! insert関数
nums.insert(2,55)   #? 3番目の要素に 55を挿入
print(nums)