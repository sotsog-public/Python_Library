#関数の確認
x = 2
y = x * x
print(y)

#関数化してみる
def test(x):
    y = x * x
    print(y)
#関数の呼び出し
test(4)
#関数　戻り値あり
def retest(x):
    y = x * x
    return y
#関数の呼び出し

print(retest(5))
#クラス　インスタンス　オブジェクト指向

#class

class Lesson1():
    age = 30
    name = '田中'

#インスタンス化
l = Lesson1()

print(str(l.age) + '歳')
print(l.name)

class Lesson2:
    age = 30
    name = '田中'
    def __init__(self):
        self.age = self.age + 1


    def show(self):
        print(self.age,self.name)
        
#インスタンス化
l2 = Lesson2()

print('showの実行前')
print(l2.age,l2.name)

print('showを実行')
l2.show()


