import tkinter as tk

root = tk.Tk()
root.geometry("1920x1080")

#! 定義した順ではなく、下のpackやgridした順に画面に表示される
label0 = tk.Label(root,text="初めてのゼロ",font=("Arial",30))
label1 = tk.Label(root,text="初めてのアコム",font=("Arial",30))
label2 = tk.Label(root,text="初めてのカウカウファイナンス",font=("Arial",30))
label3 = tk.Label(root,text="初めてのウシジマくん",font=("Arial",30))
label4 = tk.Label(root,text="初めての物乞い",font=("Arial",30))
label5 = tk.Label(root,text="初めての臨死体験",font=("Arial",30))


# label1.pack()
# label1.grid(row=0, column=0)
# label2.grid(row=1, column=0)
# label3.grid(row=2, column=0)
# label4.grid(row=3, column=0)
# label5.place(x=0, y=200)

# label.grid(row=4)
# label.place(len(5))

def button_click():
    text = entry.get()
    print(text)

button = tk.Button(root, text="ボタン",font=("Arial",30),command=button_click) #* 関数名だけ付ける。
# button.pack()
entry = tk.Entry(root, font=("Arial",30))
# entry.pack()



#! 画像を表示
load_image = tk.PhotoImage(file="py_test\\body_chou_bad.png")
img = tk.Label(root, image=load_image)
# img.pack()

#! 複数行のメッセージ
msg = tk.Message(
    root,
    text="「怪文書」とは本来発行者が明かされぬままに出回る匿名の文書…とりわけリークや内部告発の類を指すものであることは言うまでもない。一方で情報共有を目的とする一部のコミュニティでは、暇を持て余した者の手慰みとして短編小説の範をとったSS…つまりはショートストーリーが投稿され、これが本来の怪文書に取って代わって膾炙するようになったという経緯が存在する。これは特筆すべき興味深い事実だ。なぜ裂獣やシーボーンではなく我々だけが文字を紬ぎ、絵を描き、詩を歌うのか?それらが我々の「理性」によって生み出されるものだからというのがこの種の問に対する普遍的な回答だ。つまり怪文書でさえも我々が星空の下、この大地で生きてきた証に他ならないと言えるだろう。だがそうして書かれたものの中には甚だ理性的とは言えない、半ば正気を失っていなければ書けない支離滅裂な内容が含まれているのもまた事実だ。「怪文書」は理性によって生み出される…しかし「怪文書」からは理性が失われている…これは実に皮肉な示唆に富んでいると思わないか?ドクター。",
    font=("Arial",12),
    bg="white",
    width=300
)
# msg.pack()

canvas = tk.Canvas(root,bg="black",width=500,height=500)
canvas.pack()

canvas.create_text(0,0,text="NowLoading",fill="white",font=("Arial",20),anchor="ne")



root.mainloop()
