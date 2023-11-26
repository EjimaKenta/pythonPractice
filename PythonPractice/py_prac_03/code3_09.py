score = int(input("試験点数を言え>> "))

if score < 0 or score > 100:
    print("異常。再試行")
elif score >= 60:
    print("合格、精進")
else:
    print("残念、不合格、教育、死刑")