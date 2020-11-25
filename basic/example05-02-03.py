# codeing:utf-8
# import random

# a = random.randint(0,9)
# print(a)

# b = input("数を入れてね＞")
# if a == b:
#   print("当たり")
# else:
#   print("はずれ")

#同じ数字にしてもはずれと出る
#数値と文字列の問題

import random

a = random.randint(0,9)
print(a)

b = int(input("数を入れてね＞"))
if a == b:
  print("当たり")
else:
  print("はずれ")
