text = input("今日何実行奴？>> ")
with open("diary.txt","a",encoding="utf-8") as file:
    file.write(text + "\n")