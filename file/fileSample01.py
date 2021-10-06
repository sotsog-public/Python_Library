f = open('sample.txt','r')#ファイルを開く　rは read(読み込み)
content = f.read() #データの読み込みを行いcontent内に格納
print(content)

#任意の位置のデータを取得する
print(content[0])
#print(content[1])
print(content[2])
print(content[10])
print(content[12])
