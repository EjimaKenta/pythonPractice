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
button.pack()
entry = tk.Entry(root, font=("Arial",30))
entry.pack()

root.mainloop()
