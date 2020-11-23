# coding:utf-8
import random

a = random.randint( 0 , 9 )
print(a)

b = int(input("数を入れてね＞"))

if a == b:
  print("あたり")
else:
  print("はずれ")

#a1 = random.randint( 0 , 9 )
#a2 = random.randint( 0 , 9 )
#a3 = random.randint( 0 , 9 )
#a4 = random.randint( 0 , 9 )

#print(str(a1)+str(a2)+str(a3)+str(a4))

a = [random.randint(0,9),
     random.randint(0,9),
     random.randint(0,9),
     random.randint(0,9)]
print(str(a[0])+str(a[1])+str(a[2])+str(a[3]))

b = input("数を入れてね>")
print(b[0])
print(b[1])
print(b[2])
print(b[3])

b = input("数を入れてね＞")
if len(b)!=4:
  print("４桁の数字を入力してください")


