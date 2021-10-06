#python の配列について
a = [1, 2, 3, 4]
print(a)

#条件分岐 if分
z = 1
if z == 1:
    print('zは1です')

if z == 2:
    print('zは1ではありません')

print('if分の処理は終わっています')
#等号　==

#大なり小なり > < 
small = 2
big = 4
mid = 2

if small < big:
    print('smallの方が小さいです')

if small > big:
    print('bigの方が小さいです')

if small >= mid:
    print('smallはmid以上です')
if small <= mid:
    print('smallはmid以下です')

#論理演算子　and(かつ), or(または)
if small < big and small == mid:
    print('条件一に合致しています')

if small < big and small != mid:
    print('条件二に合致しています')

if small < big or small != mid:
    print('条件三に合致しています')

