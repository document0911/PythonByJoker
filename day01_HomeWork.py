# 1.
# celsius = float ( input ("请输入一个摄氏温度"))
# fahrenheit = float ((9 / 5) * celsius + 32)
# print ("华氏温度：%.1f"%fahrenheit)

# 2.
# import math
# radius = float ( input ("请输入半径"))
# length = float ( input ("请输入高"))
# area = float (radius * radius * math.pi)
# volume = float (area * length)
# print ("The area is%f"%area)
# print ("The volume is%.1f"%volume)

# 3.
# feet = float ( input ("请输入英尺数"))
# meters = float ( feet * 0.305)
# print ("%f feet is%.4f meters"%(feet,meters))

# 4.
# M = float ( input ("请输入水量"))
# initialTemperature = float (input ("请输入水的初始温度"))
# finalTemperature = float (input ("请输入水的最终温度"))
# Q = float (M * (finalTemperature - initialTemperature) * 4184)
# print ("The energy needed is %.1f"%Q)

# 5.
# chaEr = float ( input ("请输入差额"))
# nianLiLv = float ( input ("请输入年利率"))
# interest = float ( chaEr * (nianLiLv / 1200))
# print ("The interest is %.5f"%interest)

# 6.
# v0 = float ( input ("请输入初速度"))
# v1 = float ( input ("请输入末速度"))
# t = float ( input ("请输入变化所占用的时间"))
# a = float ( (v1 - v0) / t)
# print ("平均加速度:%.4f"%a)

# 7.
# i = 0
# a = [0,1,2,3,4,5]
# sum = 0
# money = int ( input ("请输入每月存款金额"))
# for i in a:
#     sum = float ( ( money + sum) * (1 + 0.00417))
#     i = i + 1
#     print(i)
#     print(sum)
# print ("账户总额：%f"%sum) 

# 8.
# number = int ( input ("请输入一个整数"))
# if number >= 1000 or number <= 0:
#     print ("输入范围有误，请重新输入")
# else:
#     bai = int ( number / 100)
#     shi = int ( ( number / 10) % 10)
#     ge = int ( number - bai * 100 - shi * 10)
#     sum = int ( bai + shi + ge)
#     print("数字之和:%d"%sum)

# 9.
# import math
# r = float ( input ("请输入顶点到中心的距离"))
# s = float ( 2 * r * math.sin ( math.pi / 5))
# area = float ( ( 5 * s * s) / ( 4 * math.tan ( math.pi / 5))) 
# print("五边形的面积：%.2f"%area)

# 10.
# import numpy as np
# import math
# x1 = float ( input ("请输入经度x1 :"))
# y1 = float ( input ("请输入纬度y1 :"))
# x2 = float ( input ("请输入经度x2 :"))
# y2 = float ( input ("请输入纬度y2 :"))
# radius = 6371.01
# d = float ( radius * np.arccos(math.sin(x1) * math.sin(x2) + math.cos(x1) * math.cos(x2) * math.cos(y1 - y2)))
# print("大圆距离:%f"%d)

# 11.
# import math
# s = float ( input ("请输入五角形的边长"))
# area = float ( ( 5 * s * s) / ( 4 * math.tan( math.pi / 5)))
# print("五角形的面积：%f"%area)  

# 12.
# import math
# n = int ( input ("请输入边数"))
# s = float ( input ("请输入边长"))
# area = float ( ( n * s * s) / ( 4 * math.tan( math.pi / 5)))
# print("面积为：%f"%area)

# 13.
# number = int ( input ("请输入一个整数"))
# if number > 127 or number < 0:
#     print ("输入错误，请重新输入")
# else:
#     letter = chr (number)
#     print ("The character is %s"%letter)

# 14.
# name = str ( input ("请输入姓名"))
# time = float ( input ("请输入一周工作时间"))
# money = float ( input ("请输入每小时报酬"))
# federal = float ( input ("请输入联邦预扣税率"))
# state = float ( input ("请输入州预扣税率"))
# pay = float ( money * time)
# federalRate =  float ( pay * federal)
# stateRate = float ( pay * state)
# deduction = float ( federalRate + stateRate)
# netPay = float ( pay - deduction)
# print("Employee Name:%s"%name)
# print("Hours Worked:%.1f"%time)
# print("Pay Rate:%.2f"%money)
# print("Gross Pay:%.1f"%pay)
# print("Deductions:")
# print("  Federal Withholding (20.0%%):%.1f"%federalRate)
# print("  State Withholding (9.0%%):%.2f"%stateRate)
# print("  Total Deduction:%.2f"%deduction)
# print("Net Pay:%.2f"%netPay)

# 15.
# number = str ( input("请输入一个四位整数"))
# for i in number[::-1]:
#     print(i,end="")

# 16.
# str1 = input("请输入一个字符串")
# for i in str1:
#     print ( chr ( ord ( i) - 14), end="")