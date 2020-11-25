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

#b = input("数を入れてね>")
#print(b[0])
#print(b[1])
#print(b[2])
#print(b[3])

#b = input("数を入れてね＞")
#if len(b)!=4:
  #print("４桁の数字を入力してください")

isok = False
while isok == False:
  b = input("数を入れてね")
  if len(b) !=4:
    print("4桁の数字を入れてください")
  else:
    isok = True

print(b[0])
print(b[1])
print(b[2])
print(b[3])

#import re

#hit = 0
#if a[0] == int(b[0]):
  #hit = hit + 1
#if a[1] == int(b[1]):
  #hit = hit + 1
#if a[2] == int(b[2]):
  #hit = hit + 1
#if a[3] == int(b[3]):
  hit = hit + 1

# hit = 0
# for i in range(4):
#   if a[i] == int(b[i]):
#     hit = hit + 1


