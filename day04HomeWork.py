# 1.   待优化,未实现动态输入数字
# def function_compare(_list):
#     _list1 = sorted(_list)
#     _max = _list1[-1]
#     function_list(_list,_max)
# def function_list(_list,_max):
#     for i in _list:
#         if i >= _max - 10:
#             print("%d    A"%i)
#         elif i >= _max - 20:
#             print("%d    B"%i)
#         elif i >= _max - 30:
#             print("%d    C"%i)
#         elif i >= _max - 40:
#             print("%d    D"%i)
#         else :
#             print("%d    E"%i)

# _list = [40,55,70,58]
# function_compare(_list)

# 2.
# def function_list():
#     _list = [10,20,30,40,50]
#     print(_list[::-1])
# function_list()

# 3.
# def function_list(_list):
#     res = {}
#     for i in _list:
#         res[i] = _list.count(i)
#     print(res)

# function_list([2,5,6,5,4,3,23,43,2])

# 4.
# def function_compare(_list , average):
#     gao = 0
#     di = 0
#     for i in _list:
#         if i > average:
#             gao += 1
#         else :
#             di +=1
#     print("%d      %d"%(gao,di))
# def function_list(_list):
#     _sum = 0
#     for i in _list:
#         _sum += int(i)
#     average = _sum / len(_list)
#     function_compare(_list , average)
# function_list(_list = [10,20,30,40,50])

# 5.

# 6.
# def function_compare(_list):
#     _li = _list.index(min(_list))
#     print(_li)
# _li = input("输入字符串：")
# function_compare(_li)

# 7.

# 8.
# def function_list(_list):
#     _listb = []
#     for i in _list:
#         if i not in _listb:
#            _listb.append(i)
#     print(_listb)

# function_list(_list = [1,2,3,2,1,6,3,4,5,2])

# 9.
# 二叉树算法


# 10.
# def function_paixu(_list):
#     for i in range(len(_list)-1):
#         for j in range(len(_list)-1-i):
#             if _list[j] < _list[j + 1] :
#                 _list[j] ,_list[j + 1] = _list[j + 1] , _list[j]
#     print(_list)

# function_paixu([1,3,4,5,6,7,8,4,32,1,4])

# 11.

# 12.
# def function_compare(lines):    
#     weiyiArray=[lines[0]]
#     resultArray=[]
#     for i in range(1,len(lines)):
#         if lines[i] in weiyiArray:
#             weiyiArray.append(lines[i])
#         else:
#             if len(weiyiArray) >=3:
#                 resultArray.append([lines[i-1],len(weiyiArray)])
#             weiyiArray=[]
#             weiyiArray.append(lines[i])
#     print(resultArray)
# function_compare([1,1,1,1,3,3,4,5,5,6,5,4,3,2])

# 1.
# def function_compare():


# 2.
# def find(_str1,_str2):
#     find_ = _str2.count(_str1)
#     if find_ == 1:
#         print("shi")
#     else:
#         print("bushi")

# _str1 = str(input("输入字符串1"))
# _str2 = str(input("输入字符串2"))
# find(_str1,_str2)

# 3.
# def function_compare(_str):
#     j = 0
#     if len(_str) >= 8:
#         if _str.isalnum() == True:
#             for i in _str:
#                 if i.isdigit() == True:
#                     j += 1
#                 else :
#                     continue
#             if j >= 2:
#                 print("密码注册正确")
#             else :
#                 print("密码中数字少于两位")
#         else :
#             print("密码中包含特殊字符")
#     else:
#         print("密码长度小于8位，输入错误")

# _str3 = str(input("请输入注册密码"))
# function_compare(_str3)

# 4.
# def countLetters(s):
#     res = {}
#     for i in s:
#         res[i] = s.count(i)
#     print(res)
# _str = str(input("请输入字符串"))
# countLetters(_str)

# 5.
# def getNumber(_str):
#     _s = ''
#     for i in _str:
#         if i.isdigit() == True:
#             _s += i
#         elif i == "A" or i =="B" or i == "C" or i == "a" or i =="b" or i == "c":
#             i = "2"
#             _s += i
#         elif i == "D" or i =="E" or i == "F" or i == "d" or i =="e" or i == "f":
#             i = "3"
#             _s += i
#         elif i == "G" or i =="H" or i == "I" or i == "g" or i =="h" or i == "i":
#             i = "4"
#             _s += i
#         elif i == "J" or i =="K" or i == "L" or i == "j" or i =="k" or i == "l":
#             i = "5"
#             _s += i
#         elif i == "M" or i =="N" or i == "O" or i == "m" or i =="n" or i == "o":
#             i = "6"
#             _s += i
#         elif i == "P" or i =="Q" or i == "R" or i == "S" or i =="p" or i == "q" or i == "r" or i == "s":
#             i = "7"
#             _s += i
#         elif i == "T" or i =="U" or i == "V" or i == "t" or i =="u" or i == "v":
#             i = "8"
#             _s += i
#         elif i == "X" or i =="Y" or i == "Z" or i == "W" or i =="w" or i == "x" or i == "y" or i == "z":
#             i = "9"
#             _s += i
#         else :
#             i.sorted(i)
#             continue
#     print(_s)
# _s = str(input())
# getNumber(_s)

# 6.
# def reverse(s):
#     print(s[::-1])
# _str = str(input("输入字符串"))
# reverse(_str)

# 7.
# def function_compare(_str):
#     com = _str.isdigit()
#     if com == True:
#         if len(_str) == 16:
#             print("合法")
#         else:
#             print("位数不符合，不合法")
#     else :
#         print("不合法")
# _str = str(input("输入信用卡号"))
# function_compare(_str)

# 8.
# def function_compare(_str):
#     _sum = 0
#     for i in range(len(_str)):
#         if i % 2 == 0:
#             _sum += int(_str[i]) * 3
#         else :
#             _sum += int(_str[i])
#     _str13 = str(10 - (_sum % 10))
#     if _str13 == "10":
#         _str13 = "0"
#         print(_str + _str13)
#     else:
#         print(_str + _str13)
# _str = str(input())
# function_compare(_str)
