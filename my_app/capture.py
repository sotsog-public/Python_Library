#ここで内部の動きを実装する
import cv2
import numpy as np
from PIL import ImageGrab#スクリーンショットを取るためのライブラリ
#時間を扱うためのライブラリからsleepをインポート
from time import sleep
import time
#フォルダの作成やファイルの削除を行うのでos
import os
#現在の日付時刻を取得することができるライブラリ
import datetime

#一致率の目安を定義する
per = 99#99パーセント以上一致していたら画像を保存しない
per = float(per)
per = per / 100#0.99になる

#何秒ごとにスクリーンショットを取るかを定義する
s_time = 3#3秒ごとにスクリーンショットを撮影
s_time = int(s_time)#int型に変換しておく

#ユーザーにメッセージを表示する
print('収集を終了するためにはキーボードの[Ctrl]と[C]を同時に押してください。')

#収集した画像を保存するためのフォルダを作成
#フォルダの名前に収集開始時刻を入れておく
now = datetime.datetime.now()#現在の日付時刻を取得
file_name = 'box_{0:%Y%m%d%H%M%S}'.format(now)
local = './slide_cap/' + file_name
#フォルダを作成していく

try:
    os.makedirs(local)
#slide_capが存在していなければslide_capも作る（２つフォルダを作成する場合がある）
#うまくいかなかったときの処理
except FileExistsError:
    pass#エラーが起きると何もせずにスキップする

#現在の時刻を取得
now_temp = datetime.datetime.now()#現在の日付時刻を取得
t_temp = '{0:%Y%m%d%H%M%S}'.format(now)

#ここで実際にスクリーンショットを撮影する
#一番最初のスクリーンショットを作成する
temp_image = ImageGrab.grab()#grabメソッドでPC内のスクリーンショット撮影することができる
#撮影した画像を保存(jpg形式)
temp_image.save(local + './' + t_temp + 'sh.jpg')

#撮影した写真はまだ今後使用するのでOpencv上で扱えるようにしておく
temp = cv2.imread(local + './' + t_temp + 'sh.jpg')
#後ほど画像の一致率を比較するのでヒストグラム化しておく
temp_image_hist =cv2.calcHist([temp],[0],None,[256],[0, 256])#ヒストグラム化

count = 1
#繰り返し処理を行う　途中でストップできるようにキーボードインタラプトを使う
try:
    #今回はwhileを使って繰り返し処理を行う
    while count < 100: 
        #3秒プログラムを停止する
        sleep(1)
        #新しいスクリーンショットを撮影
        new_image = ImageGrab.grab()
        #現在の時刻を取得
        now_new = datetime.datetime.now()
        #フォーマットを調整して文字列としておく
        t_new = '{0:%Y%m%d%H%M%S}'.format(now_new)
        #スクリーンショットをとった画像を保存
        new_image.save(local + './' + t_new + 'sh.jpg')
        #保存した画像を読み取ってopencv上で使えるようにします
        new = cv2.imread(local + './' + t_new + 'sh.jpg')
        #ヒストグラム化しておく
        new_image_hist = cv2.calcHist([new], [0], None , [256], [0,256])

        #ここまでで下準備は終了　ここから実際に比較を行う
        #比較を行う
        if cv2.compareHist(new_image_hist,temp_image_hist,0) > per: #比較した結果が指定した基準より大きい（つまりtemp newが似ている）
            print('一致率')
            print(cv2.compareHist(new_image_hist,temp_image_hist,0))
            #新しい画像(new)はひとつ前に取ったスクリーンショットと類似しているので消す
            temp_image_hist = new_image_hist#temp_imageの更新
            #似ているので削除
            os.remove(local + './' + t_new + 'sh.jpg')
        else:#似ていない場合
            # 削除を行わない
            print('一致率')
            print(cv2.compareHist(new_image_hist,temp_image_hist,0))
            #temp_image_histを新しいものに更新していく
            temp_image_hist = new_image_hist
            print('一致率が低いので画像を保存しました。')#保存した画像を削除しませんでした。
except KeyboardInterrupt:
    print('収集を終了しました。')