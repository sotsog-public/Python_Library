f = open('sample.txt','r')#ファイルを「読み取りモード」で開く

#forを使って一行ずつ読み取る
for line in f:
    line = line.rstrip()#改行の削除
    print(line)