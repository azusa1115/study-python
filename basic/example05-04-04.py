# coding:utf-8
import random

isok = False
while isok == False:
  b = input("数を入れてね＞")
  if len(b) != 4:
    print("４桁の数字を入れてください")
  else:
    kazuok = True
    for i in range(4):
      if (b[i] < "0") or (b[i] > "9"):
        print("数字ではありません")
        kazuok = False
        break
    if kazuok:
      isok = True

print(b[0])
print(b[1])
print(b[2])
print(b[3])
