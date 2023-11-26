"""
#! 標準ライブラリを使ったコピー文
import shutil
shutil.copyfile("C:\\Users\\0719AM\\Desktop\\sample.txt","C:\\Users\\0719AM\\Desktop\\sampleCopy.txt")
"""

#! 模範解答
with open ("copy.txt","w",encoding="UTF-8") as copy_file:
    with open("diary.txt","r",encoding="UTF-8") as file:
        copy_file.write(file.read())