#opencvをimportする
import cv2 
#画像を扱うので画像を取り込む
sample01 = cv2.imread('sample01.jpg')
sample02 = cv2.imread('sample02.jpg')
sample03 = cv2.imread('sample03.jpg')
sample04 = cv2.imread('sample04.jpg')
sample05 = cv2.imread('sample05.jpg')
#これで画像を扱うことができるようになった

img_size = (300,300)

#画像のサイズを変更する
s01_resize = cv2.resize(sample01, img_size)
s02_resize = cv2.resize(sample02, img_size)
s03_resize = cv2.resize(sample03, img_size)
s04_resize = cv2.resize(sample04, img_size)
s05_resize = cv2.resize(sample05, img_size)

#比較するために画像をヒストグラム化する

s01_hist = cv2.calcHist([s01_resize],[0],None,[256],[0,256])
s02_hist = cv2.calcHist([s02_resize],[0],None,[256],[0,256])
s03_hist = cv2.calcHist([s03_resize],[0],None,[256],[0,256])
s04_hist = cv2.calcHist([s04_resize],[0],None,[256],[0,256])
s05_hist = cv2.calcHist([s05_resize],[0],None,[256],[0,256])

#すべての画像を比較してみる
img_list = [s01_hist, s02_hist, s03_hist, s04_hist ,s05_hist]
#繰り返し処理(for)を活用してすべての画像を総当たりで比較
for i in img_list:
    for j in img_list:
        print(cv2.compareHist(i,j,0))
