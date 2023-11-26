
#! print関数に数値を書く P34
print(1)
print(10)
print("\n")

#! 加算と減算 P35
print(1 + 1)    #?加
print(10 - 2)   #?減
print("\n")

#! 文字列の演算 P36
print("1" + "1")
print("\n")

#! 文字列演算の応用 P38
print("python" + "の世界へようこそ")
print("逃げちゃダメだ"*8)
print("\n")

#! 文字列の途中で改行する p39
print("はじめまして松田です。体を動かすのが好きです")
print("はじめまして\n松田です\n体を動かすのが好きです")
print("引用符には\' と \" があります。")
print("コメントにもエスケープキーを適応してやるぜ！\#無意味")
print("\n")

#! 同じ式が何度も登場してしまう p44
print("半径が3cmの円の直径は、")
print(3 * 2)
print("その円の円周の長さは、直径×円周率で求まるため、")
print(3 * 2 * 3.14)
print("\n")

#! 変数の利用 p45
name = "松田"   #* str
ageP45 = 29        #* int
print(f"{name}を名乗る男({ageP45})")
print("\n")

#! 変数を利用して1-6を改善(利用版) p47
radius = 3  #* 半径(int)
diameter = radius * 2 #*直径(int)
pi = 3.14 #* 円周率(float)

    #? int+strでprintすることはできない
    #? "str" , int , "str"と、「,」を活用する
    #? フォーマット 「 f"str {int変数} str" 」を使っても組み合わせ可能
print("半径が",radius,"cmの円の直径は",radius*2,"cm、")
print("その円の円周の長さは、直径×円周率で求まるため、")
print(f"円周は {radius * diameter * pi} cm")
print("\n")

#! 変数の上書き P50
ageP50 = 20
print("浅木の年齢は",ageP50,"歳")
ageP50 = 24
print("うそ、本当は",ageP50,"歳")
print("\n")

#! アンパック代入 P52
name, ageP52 = '浅木', 24
print(name)
print(ageP52,"歳")
print("\n")

#! 浅木さんの年齢を予想するPG P54
ageP53 = 24
print("浅木先輩の今年の年齢は…")
print(ageP53,"歳")
ageP53 += 1
print("来年は")
print(ageP53,"歳")
ageP53 += 1
print("再来年は")
print(ageP53,"歳")

#! キーボードから値を入力する(input関数) P58
name = input("あなたの名前を入力してください。>>")
print("おお、",name,"よ、そなたがくるのを待っておったぞ！")
