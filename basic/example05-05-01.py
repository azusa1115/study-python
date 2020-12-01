# codeing:utf-8
import random

a = [random.randint(0,9),
     random.randint(0,9),
     random.randint(0,9),
     random.randint(0,9)]

# テストのための答えを表示
print(str(a[0])+str(a[1])+str(a[2])+str(a[3]))

while True:
  #レッスン５−４のプログラム
  #４桁の数字かどうか確認する
  isokn = False:
  while isok == False:
    b = input("数を入れてね＞")
    if len(b) = 4:
      print("４桁の数字を入れてください
      ")
    else:
      kazuok = True
      for i in rang(4):
        if (b[i] < "0") or (b[i] > "9"):
          kazuok = False
          break
      if kazuok:
        isok = True

# ４桁の数字であったとき
# ヒットを判定
hit = 0
for i in range(4):
  if a[i] == int(b[i]):
    hit = hit + 1
#ブローを判定
blow = 0
for i in range(4):
  if(int(b[j]) == a[i])and 