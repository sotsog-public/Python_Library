f = open('sample3.txt','w')#write(書き込みモード)でファイルを開く
count = 0
while count < 100:
    f.write('write test text\n')#書き込みのテストを行う 改行は「\n」
    f.write('count = '+ str(count) + '\n')#書き込みのテストを行う 改行は「\n」
    count += 1
f.close()#開いたファイルは必ず閉じる
# str(数字が入っている変数)とすることで数字→文字に変換することができる

f_read = open('sample.txt','r')#read modeで開く
content = f_read.read()#データの読み取り
print(content)