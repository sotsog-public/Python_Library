#socketをインポート
import socket

#ソケット（通信を行うための機械）
so = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print('start server')
#相手から通信を受信する準備を行う
so.bind(('',5555))#何も指定しないと127.0.0.1になる
so.listen(10)#キューを用意
c, addr = so.accept()#通信を受け入れる
print('connected')

#通信の内容
while True:
    #データを受信
    data = c.recv(1024)
    #受信したデータを文字列に変換
    dataStr = str(data, encoding='utf-8')
    #もし相手がexitと送って来たら繰り返し処理を終了する。
    if dataStr == 'exit':
        break
    #受け取ったデータを表示
    print('client:' + dataStr)
    #受信したデータをオウム返し
    c.send(bytes('I recv your msg:' + dataStr,encoding='utf-8'))
    #socketを閉じる
    so.close()
