# coding:utf-8
import random

isok = False
while isok == False:
  b = input("数を入れてね＞")
  if len(b) != 4:
    print("４桁の数字を入力してください")
  else:
    isok = True

#フラグ