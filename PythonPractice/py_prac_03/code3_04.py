name = input("名乗れ>> ")

print(f"こんにちは、{name}")

food = input(f"{name}、好物を述べよ")

if "カレー" in food:
    print("カレーは良い")
else:
    print(f"{food}でもまぁ良い")