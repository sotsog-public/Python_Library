#現在の日付時刻を取得してみる
import datetime

now = datetime.datetime.now()#現在の日付時刻を取得
print('{0:%Y%m%d%H%M%S}'.format(now))