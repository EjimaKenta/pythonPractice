
#! identity の確認
score1 = [80, 40, 50]
score2 = [80, 40, 50]
print(f"score1のidentity:{id(score1)}")
print(f"score2のidentity:{id(score2)}")

if score1 == score2:
    print("s1とs2は同一存在")
else:
    print("s1とs2は違う存在")

if id(score1) == id(score2):
    print("s1とs2は同一存在")
else:
    print("s1とs2は違う存在")
