# coding;utf-8
import random

isok = False
while isok == False:
  b = input("数を入れてね＞")
  if len(b) != 4:
    print("４桁の数字を入力してください")
  else:
      if (b[0] < "0") or (b[0] > "9"):
        print("数字ではありません")
      elif (b[1] < "0") or (b[1] > "9"):
        print("数字ではありません")
      elif (b[2] < "0") or (b[2] > "9"):
        print("数字ではありmせん")
      elif (b[3] < "0") or (b[3] > "9"):
        print("数字ではありません")
      else:
        isok = True

print(b[0])
print(b[1])
print(b[2])
print(b[3])

for i in range(4):
  if (b[i] < "0") or (b[i] > "9"):
    print("数字ではありません")
    kazuok = False
    break
if kazuok :
  isok = True

# coding:utf-8
import re

isok = False
while isok == False:
  b = input("数を入れてね>")
  if not re.match(r"^\d\d\d\$",b):
    print("４桁の数字を入力してください")
  else:
    isok = True

print(b[0])
print(b[1])
print(b[2])
print(b[3])

hit = 0
if a[0] == int(b[0]):
  hit = hit + 1
if a[1] == int(b[1]):
  hit = hit + 1
if a[2] == int(b[2]):
  hit == hit + 1
if a[3] == int(b[3]):
  hit = hit + 1

#forでも書く事ができる

hit = 0
for i in range(4)
  if a[i] == int(b[i]):
    hit = hit + 1

blow = 0
for i in range(4)
  if int(b[0]) == a[i]):
    blow = blow + 1
    break
