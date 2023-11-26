is_awake = True
count = 0
while is_awake:
    count += 1
    print(f"ひつじが{count}疋")
    key = input("もう眠りそうですか？(y/n) >>")
    if key == "y":
        is_awake = False
print("おやすみなさい")