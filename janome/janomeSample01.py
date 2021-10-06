from janome.tokenizer import Tokenizer#トークン解析を行うための解析器をインポート
token = Tokenizer() #tokenの中に解析器をセットする
#形態素解析を行う
tokens = token.tokenize('恥の多い生涯を送って来ました。自分には、人間の生活というものが、見当つかないの\
です。自分は東北の田舎に生れましたので、汽車をはじめて見たのは、よほど大きくなってから\
でした。自分は停車場のブリッジを、上って、降りて、そうしてそれが線路をまたぎ越えるため\
に造られたものだという事には全然気づかず、ただそれは停車場の構内を外国の遊戯場みたいに、\
複雑に楽しく、ハイカラにするためにのみ、設備せられてあるものだとばかり思っていました。しか\
も、かなり永い間そう思っていたのです。ブリッジの上ったり降りたりは、自分にはむしろ、ずいぶん\
')

for token in tokens:
    print(token)#実際に解析結果を表示する