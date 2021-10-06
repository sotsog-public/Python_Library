#socketはあらかじめpythonに組み込まれいるためインストールは不要です
import socket#socketをインポート

# ソケットを作成
so = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#通信を行うための機械
#実際に接続を行う
so.connect(('127.0.0.1',5555))#ipアドレスが127.0.0.1 ポートが5555
#住所のようなもの

while True:
    msg = input('メッセージを作成(exitで終了)')#相手に送るメッセージの作成
    #作成したメッセージを送る
    so.send(bytes(msg, encoding = 'utf-8'))
    #相手からのメッセージを受信
    data = so.recv(1024)
    #受け取ったデータの表示
    print('recv:'+str(data,encoding='utf-8'))
    #もし自分が入力したデータがexitなら終了させる
    if msg == 'exit':
        break