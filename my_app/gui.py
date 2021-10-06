#見た目の部分を作成するためにtkinterを使う
import tkinter as tk
#GUI（見た目）の部分を作成します
win = tk.Tk()#アイテムを配置するためのキャンバス
win.minsize(300,350)#最小サイズを指定してwinを作る
c = tk.Canvas(win)#キャンバスを作成
#作成したキャンバスを配置する
c.place(x = 300,y = 0)
#ここにキャンバス内に配置したいエレメントを記述する
#アプリのタイトルを記述する
label1 = tk.Label(win, text = 'Zoom会議資料　自動収集アプリ')
label1.place(x = 5, y = 5)

#スクリーンショットの撮影間隔（秒）をユーザーに求める
label2 = tk.Label(win, text = 'スクリーンショットの撮影間隔(秒）を入力してください')
label2.place(x = 5 ,y = 50)

#ユーザーが入力を行うためのボックスを用意する
input_time = tk.Entry(win,width = 20)
input_time.place(x = 5, y = 100)
#初期値を設定する
input_time.insert(0,"30")

#スクリーンショットを開始するためのトリガーとなるボタン
btn = tk.Button(win,text = '開始')
btn.place(x = 30, y = 165)

win.mainloop()