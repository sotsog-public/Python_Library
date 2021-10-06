#繰り返し処理 (while分)

n = 0
while n < 3:
    print(str(n) + '回目の繰り返しです')
    #n += 1
    n = n + 1

#繰り返し処理　(for分)

for i in [0,1,2,3,4]:
    print(str(i) + 'にアクセスしています')

for i in range(0,1000):
    print(str(i) + 'にアクセスしています[2]')

list = {'apple':'田中', 'orange':'佐藤','melon':'佐々木'}
for n in list.items():
    print(n)

list1 = [1,2,3,4]
print(list1)

list2 = [[1,2,3],[4,5,6]]
print(list2)