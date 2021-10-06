#GUI操作のためのプログラム
#tkinterをインポート
import tkinter as tk
# tkとして扱える
#GUI表示のためのキャンバスを用意する
def click():
    print('you click !')
    label2 = tk.Label(canvas,text = 'you click !')
    label2.place(x = 20,y = 80)

canvas = tk.Tk()
canvas.title('テストキャンバス')
canvas.minsize(800,400)
#文字列を表示してみる
label = tk.Label(canvas, text = 'テスト用のテキスト')
label.place(x = 20,y = 20)
label1 = tk.Label(canvas, text = 'テスト用のテキスト')
label1.place(x = 20,y = 50)

button = tk.Button(canvas, text = 'click me',command = click)
button.place(x = 20,y = 100)

canvas.mainloop()