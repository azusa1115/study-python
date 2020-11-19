#for文

for a in [1,2,3,4,5]:
  print(a)
  print("こんにはち")

for a in range(1,5+1):
  print(a)
  print("こんにちは")

for a in range(100):
  print( a + 1 )
  print("こんにちは")

# while文（繰り返す）
#ずっと動きっぱなしになったらこんとろーる＋cキー
#else


total = 0
a = 1
while total <= 50:
  total = total +a
  a = a + 1
print(total)

# and 二つの条件が成り立つ時
# or 二つの条件のいずれかが成り立つ時
# not 条件の否定

for a in range( 1 , 10 + 1 ):
  print(a)
  if a % 2 == 0:
    print("○")
  if a % 3 == 0:
    print("×")
  if (a % 2 ==0 ) and (a % 3 == 0):
    print("△")

#％は余りを計算する演算子。余りがゼロならその数の倍数でsるということ
#while True 永遠に繰り返す

while True:
  total = total + a
  a = a + 1
  if total  > 50:
    break
  print(total)

#★４−６（p１０６）

def tashizan(a,b):
  total = 0
  for i in range(a,b+1):
    total = total + i
  return total

c = tashizan(1,5)
print(c)

#変数

c = tashizan(1,5)

total = 0
for i in range(a,b,+1):
  total = total + 1

a = "abc"

def test():
  print(a)
  return

test()
print(a)

#4-7 p116

import calendar as c
print(c.month(2017,12))

from calendar impoet mpnth


