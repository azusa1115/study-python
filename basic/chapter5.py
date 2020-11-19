# coding:utf-8

import random
a = random.randint(0,9)
print(a)

#これで実行するたびに違う数字が出てくる

b = input("数を入れてね＞")
print(b)

#※※inputで入力したものは、文字列として認識される

b = int(input("数を入れてね＞"))

if a == b:
  print("あたり")
else:
  print("はずれ")

# coding:utf-8
import random

a = [random.randint(0,9),
     random.randint(0,9),
     random.randint(0,9),
     random.randint(0,9)]

print(str(a[0]) + str(a[1]) + str(a[2]) + str(a[3]))
#str付けないとそのまま計算されてしまうから気を付ける

# coding:utf-8
import random

isok = False
while isok == False:
  b = input("数を入れてね＞")
  if len(b) != 4:
    print("４桁の数字を入力してください")
  else:
      isok = True

print(b[0])
print(b[1])
print(b[2])
print(b[3])








