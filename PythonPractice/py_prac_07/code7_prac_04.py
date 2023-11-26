
#! (1)入力された3つの整数のうち、大きい値を表示する
inputNum1 = int(input("半角数字1>> "))
inputNum2 = int(input("半角数字2>> "))
inputNum3 = int(input("半角数字3>> "))
Nums = [inputNum1, inputNum2, inputNum3]

print(f"一番大きい数字 -> {max(Nums)}")

#! (2)円周率 3.141519 について、小数点以下第1位から第5位を四捨五入した値をそれぞれ表示
pi = 3.141519
print(f"第1位四捨五入{round(pi,0)}")
print(f"第2位四捨五入{round(pi,1)}")
print(f"第3位四捨五入{round(pi,2)}")
print(f"第4位四捨五入{round(pi,3)}")
print(f"第5位四捨五入{round(pi,4)}")
