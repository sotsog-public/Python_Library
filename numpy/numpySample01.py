#numpyの基本的な使用を学習します
import numpy as np
a_1d = np.array([1,2,3,4,5,6,7,8])
print(a_1d)#一次元の配列
#二次元の配列も作ってみる
a_2d = np.array([[1,2,3],[5,6,7]])
print(a_2d)
#二次元配列を一次元として扱う方法
print(np.ravel(a_2d))
#配列から特定のデータのみを取り出す
print(a_1d[a_1d > 3])#1より大きいデータを取得する
print(a_2d[a_2d > 2])#二次元でも行える

#部分配列にもアクセスできる
print(a_1d[2:5])#2から4個目のデータにアクセスする

#配列の演算
a = np.array([1,2,3,4])
b = np.array([5,6,7,8])

print(a + b) #配列の加算
print(a - b) #配列の減算

print(a * b)#配列の乗算　乗算であって「内積」や「外積」ではないので注意
# あくまで数値同士を演算するので
print(a / b)#配列の除算

#重要！配列の内積を求める方法
#内積はnp.dot(a,b)
print('内積を計算します\n')
print(np.dot(a,b))
#掛け算を行った後ですべての和を求めている

#三変数の計算もできる
c = np.array([2,3,4,5])
print(a + b + c)

#逆行列
c_2d = np.array([[1,3],[2,4]])
#c_2dの逆行列を求めてみる
c_2d_inv = np.linalg.inv(c_2d)#逆行列を求める
print(c_2d_inv)
print('逆行列かどうかの確認')
print(np.dot(c_2d,c_2d_inv))
#二次元配列の内積はベクトル積となる



