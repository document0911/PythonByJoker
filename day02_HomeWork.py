1.
import math 
a = float(input("输入a"))
b = float(input("输入b"))
c = float(input("输入c"))
discriminant = float(b * b - 4 * a * c)
if discriminant > 0:
    r1 = ((- b) + math.sqrt(discriminant)) / (2 * a)
    r2 = ((- b) - math.sqrt(discriminant)) / (2 * a)
    print("The roots are %f and %f"%(r1,r2))
elif discriminant == 0:
    r1 = (-b + math.sqrt(discriminant)) / (2 * a)
    print("The roots is %f"%r1)
else :
    print("The equation has no real roots")

2.
import numpy as np
num1 = np.random.choice(100)
num2 = np.random.choice(100)
_sum = int(num1 + num2)
print(num1)
print(num2)
user_sum = input("he ")
if user_sum == str(_sum):
    print("ture")
else :
    print("flase")

3.
today = int(input("Enter today’s day:"))
future = int(input("Enter the number of days elapsed since today:"))
day_sum = int(today + future)
if day_sum % 7 == 0:
    print("Today is ")
elif day_sum % 7 == 1:
    print("1")
elif day_sum % 7 == 2:
    print("2")
elif day_sum % 7 == 3:
    print("3")
elif day_sum % 7 == 4:
    print("4")
elif day_sum % 7 == 5:
    print("5")
else:
    print("6")

4.
num1 = int(input("输入数字1："))
num2 = int(input("输入数字2："))
num3 = int(input("输入数字3："))
if num1 > num2:
    if num1 > num3:
        if num2 > num3:
            print("%d>%d>%d"%(num1,num2,num3))
        else :
            print("%d>%d>%d"%(num1,num3,num2)) 
    else :
        print("%d>%d>%d"%(num3,num1,num2))
else : 
    if num2 > num3:
        if num1 > num3:
            print("%d>%d>%d"%(num2,num1,num3))
        else :
            print("%d>%d>%d"%(num2,num3,num1))
    else :
        print("%d>%d>%d"%(num3,num2,num1))

5.
rice1 = float(input("包装1大米的重量"))
money1= float(input("包装1大米的金额"))
rice2 = float(input("包装2大米的重量"))
money2= float(input("包装2大米的金额"))
if rice1 == rice2:
    if money1 > money2:
        print("包装2的价钱更好")
    else :
        print("包装1的价格更高")
else :
    money1 *= rice1 / rice2 
    if money1 >money2:
        print("包装2的价钱更好")
    else :
        print("包装1的价钱更好")

6.
month = int(input("输入月份："))
year = int(input("输入年份："))
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0 :
    if month == 2 :
        print("%d年%d月份有29天"%(year,month))
    elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12 :
        print("%d年%d月份有31天"%(year,month))
    else :
        print("%d年%d月份有30天"%(year,month))
else :
    if month == 2 :
        print("%d年%d月份有28天"%(year,month))
    elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12 :
        print("%d年%d月份有31天"%(year,month))
    else :
        print("%d年%d月份有30天"%(year,month))

7.
import numpy as np
_str = np.random.choice(["正面","反面"])
user_str = input("请输入猜测值")
if user_str == _str :
    print("正确")
else :
    print("错误")

8.
import numpy as np
diannao = np.random.choice(['0','1','2'])
wo = input("请输入石头(1)、剪刀(0)、布(2)")
if diannao == wo:
    print("平局")
elif (diannao == "0" and wo == "2") or (diannao == "1" and wo == "0") or (diannao == "2" and wo == "1"):
    print("我输了")
else :
    print("我赢了")

9.
import numpy as np
year = int(input("输入年份"))
m = int(input("输入月份"))
q = int(input("输入天数"))
j = year // 100
k = year % 100
if m == 1 :
    m = 13
    year = year - 1
    j = year // 100
    k = year % 100
    h = int((q + (26 * (m + 1)) // 10 + k + k // 4 + j // 4 + 5 * j) % 7)
    if h == 0 :
        print("星期六")
    elif h == 1 :
        print("星期日")
    elif h == 2 :
        print("星期一")
    elif h == 3 :
        print("星期二")
    elif h == 4 :
        print("星期三")
    elif h == 5 :
        print("星期四")
    elif h == 6 :
        print("星期五")
elif m == 2 :
    m == 14
    year = year - 1
    j = year // 100
    k = year % 100
    h = int((q + (26 * (m + 1)) // 10 + k + k // 4 + j // 4 + 5 * j) % 7)
    if h == 0 :
        print("星期六")
    elif h == 1 :
        print("星期日")
    elif h == 2 :
        print("星期一")
    elif h == 3 :
        print("星期二")
    elif h == 4 :
        print("星期三")
    elif h == 5 :
        print("星期四")
    elif h == 6 :
        print("星期五")
else :
    h = int((q + (26 * (m + 1)) // 10 + k + k // 4 + j // 4 + 5 * j) % 7)
    if h == 0 :
        print("星期六")
    elif h == 1 :
        print("星期日")
    elif h == 2 :
        print("星期一")
    elif h == 3 :
        print("星期二")
    elif h == 4 :
        print("星期三")
    elif h == 5 :
        print("星期四")
    elif h == 6 :
        print("星期五")

10.
import numpy as np
puke = np.random.choice(["Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"])
huase = np.random.choice(["梅花","红桃","方块","黑桃"])
print(puke,huase)

11.
num = input("输入一个三位数")
if num[0] == num[2] :
    print("是回文")
else :
    print("不是回文")

12.
num1 = int(input("输入边长1"))
num2 = int(input("输入边长2"))
num3 = int(input("输入边长3"))
_str1 = str(num1).isdigit()
_str2 = str(num2).isdigit()
_str3 = str(num3).isdigit()
if str(_str1) == 'True'  and str(_str2) == 'True' and str(_str3) == 'True' :
    if (num1 + num2) > num3 :
        print(num1 + num2 + num3)
    elif (num1 + num3) > num2 :
        print(num1 + num2 + num3)
    elif (num2 + num3) > num1 :
        print(num1 + num2 + num3)
    else :
        print("输入不合法")
else :
    print("输入不合法")

13.
zhengshu = 0
zhengshuci = 0
fushu = 0
fushuci = 0
_str = ""
while _str != "0" :
    num = int(input("输入数字："))
    if num > 0 :
        zhengshu += num
        zhengshuci += 1
    elif num < 0 :
        fushu += num
        fushuci += 1
    else :
        _str = "0" 
average = float((zhengshu + fushu) / (zhengshuci + fushuci))
print("平均数：%.2f"%average)
print("正数个数：%d"%zhengshuci)
print("负数个数：%d"%fushuci)

14.
i = 0
num = 10000
_sum = 0 
while i < 10  :
    num = float(num + num * 0.05)
    _sum += num
    i += 1
print(num)
print(_sum)

15.
j = 0
for i in range(100,1000): 
    if i % 5 == 0 and i % 6 == 0 :
        print(i,end=" ")
        j += 1
        if j == 10:
            print()
            j = 0

16.
n = 1
while n * n < 12000:
    n += 1
print(n)

n = 12000
while n * n * n > 12000:
    n -= 1
print(n)

17.
i = 1
_sum = 0
for i in range(50000,0,-1):
    _sum += 1 / i
print(_sum)

18.
i = 1 
_sum = 0
for i in range(1,100):
    _sum += (2 * i - 1) / (2 * i + 1)
print(_sum)

19.
i = 1
pai = 0
for i in range(10000):
    pai = 4 * (((-1) ** (i + 1)) / 2 * i - 1)
print(pai)

20.
_sum = 0
for i in range(1,10000):
    for j in range(1,i):
        if i % j == 0 :
            _sum += j    
    if _sum == i :
        print(i)

21.
count = 0 
for i in range(1,8):
    for j in range(1,8):
        if i != j :
            print(i,j)
            count += 1
print(count)