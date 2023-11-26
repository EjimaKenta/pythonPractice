
#! for文とrange関数を使って作れと指定あり
liftOff = 10
for count in range(10):
    print(f"{liftOff}、", end="")
    liftOff -= 1
#? ↑ 変数count用意したくせに使ってないのホントバカ

print("Lift off!")

#! 先生模範解答
for count in range(10,0,-1):
    print(f"{count}、",end="")
print("Lift off!")
#? ↑ かしこい