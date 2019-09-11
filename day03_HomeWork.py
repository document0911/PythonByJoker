# 1.
# def getPentagonalNumber(n):
#     for i in range(1,n+1):
#         num = int(((i * 3* (i - 1) / 2) + i))
#         print(num,end=" ")
#         if i % 10 == 0:
#             print()    
# getPentagonalNumber(100)

# 2.
# def sumDigits(n):
#     i = 0
#     _sum = 0
#     for i in range(n):
#         gewei = n % 10
#         _sum += gewei
#         n -= gewei
#         n = n // 10
#         i += 1
#     print(_sum)
# sumDigits(234)

# 3.
# def displaySortedNumbers(num1,num2,num3):
#     if num1 > num2:
#         if num1 > num3:
#             if num2 > num3:
#                 print("%d>%d>%d"%(num1,num2,num3))
#             else :
#                 print("%d>%d>%d"%(num1,num3,num2)) 
#         else :
#                 print("%d>%d>%d"%(num3,num1,num2))
#     else : 
#         if num2 > num3:
#             if num1 > num3:
#                 print("%d>%d>%d"%(num2,num1,num3))
#             else :
#                 print("%d>%d>%d"%(num2,num3,num1))
#         else :
#             print("%d>%d>%d"%(num3,num2,num1))

# displaySortedNumbers(10,20,30)

# 4.
# def function_Value(Amount,Rate,years):
#     rate = Rate / 100
#     for i in range(1,years + 1):
#         Amount += Amount * rate 
#         print("%d    %f"%(i,Amount))
# function_Value(1000,9,30)

# 5.
# j = 0
# def printChars():
#     global j
#     for i in range(48,123):
#         if  57 < i and i < 65 or 90 < i and i < 97:
#             continue
#         else :
#             if j != 10 :
#                 print(chr(i),end=" ")
#                 j += 1 
#             else :
#                 j = 0
#                 print()
# printChars()

# 6.
# i = 1
# def numberOfDaysInAYear(year):
#     global i
#     if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#         print("%d年有366天"%year)
#     else :
#         print("%d年有365天"%year)
#     if i != 11:
#         year += 1
#         i += 1
#         numberOfDaysInAYear(year)

# numberOfDaysInAYear(2010)

# 7.
# import math
# def function_distance(x1,y1,x2,y2):
#     distance = math.fabs(math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2))
#     print(distance)
# function_distance(4,4,1,1)

# 8.
# count = 0 
# def function_meisen(n):
#     global count 
#     for i in range(2,32):
#         if n % i == 0:
#             count += 1
#         if count == 2:
#             return True
#         count = 0

# def function_main():
#     global count 
#     for i in range(1,32):
#         if i == 1:
#             print("p         2^p-1")
#         for j in range(1,i + 1):
#             if i % j == 0:
#                 count += 1
#         if count == 2:
#             p = 2 ** i - 1
#             zhi = function_meisen(p) 
#             if zhi == True:
#                 print("%d         %d"%(i,p))
#         count = 0

# function_main()

# 9.
# import time
# def function_time():
#     geshi = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))  
#     geshi2 = time.strftime("%a %b %d %Y %H:%M:%S",time.localtime(time.time()))
#     print(geshi)
#     print(geshi2)
# function_time()

# 10.
# import numpy as np
# import random
# def function_game():
#     num1 = random.randrange(1,7)
#     num2 = random.randrange(1,7)
#     _sum = num1 + num2
#     if _sum == 2 or _sum == 3 or _sum == 12:
#         print("你输了")
#     elif _sum == 7 or _sum == 11:
#         print("你赢了")
#     else :
#         _sum = random.choice([num1,num2])
#         num3 = random.randrange(1,7)
#         if num3 + _sum == 7 :
#             print("你输了")
#         elif num3 == _sum :
#             print("你赢了")
#         else :
#             print(_sum + num3)
# function_game()
