import numpy as np
import random
import time
from datetime import datetime, timedelta
# -------------- INITIALIZATIONS --------------
inquirer = ""
location = ""
# -------------- FUNCTIONS --------------
def ganzhi(date):
    gan = ['甲', '乙', '丙', '丁', '戊', '己', '庚', '辛', '壬', '癸']
    zhi = ['子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌', '亥']
    base_date = datetime(2024, 1, 1) # known 甲子 date
    day_diff = (date - base_date).days
    gan = gan[day_diff % 10]
    zhi = zhi[day_diff % 12]
    return gan + zhi
def cnmonth(month):
    cnmonth = ['一', '二', '三', '亖', '五', '六', '七', '八', '九', '十', '十一', '十二', '十三']
    return cnmonth[month - 1]
# -------------- MAIN --------------
dec1 = str(input("Are you zhanbu for today? (y/n): "))
if dec1 == "y":
    day = ganzhi(datetime.now())
    month = cnmonth(datetime.now().month)
elif dec1 == "n":
    yearx = int(input("Input year: "))
    monthx = int(input("Input month (1-13): "))
    while monthx < 1 or monthx > 13:
        monthx = int(input("Invalid month input. Please reënter (1-13): "))
    dayx = int(input("Input date (1-31): "))
    while dayx < 1 or dayx > 31:
        dayx = int(input("Invalid day input. Please reënter (1-31): "))

    # leap year
    if monthx == 13:
        date = datetime.strptime(f"{yearx}/12/{dayx}", "%Y/%m/%d") + timedelta(days=30)
    else:
        date = datetime.strptime(f"{yearx}/{monthx}/{dayx}", "%Y/%m/%d")

    day = ganzhi(date)
    month = cnmonth(monthx)
else:
    print("Invalid input. Bye.")
    exit()

diviner = str(input("Diviner name: "))

dec2 = str(input("Is there another inquirer? (y/n): "))
if dec2 == "y":
    inquirer = str(input("Inquirer name (optional): "))

dec3 = str(input("Is there a location? (y/n): "))
if dec3 == "y":
    location = str(input("Location (optional): "))
question = str(input("Question (separate subject and predicate with a space " "): "))

# time.sleep(1)
# print("Calculating...")
# time.sleep(5)

inquirer = inquirer[0] if inquirer else ""
location = ("才" + location[0]) if location else ""
diviner = diviner[0] + "貞"
q1 = question.replace(" ", "")
q2 = question.replace(" ", "不其")
month = month + "月"

# 前辭
# 
# 占辭：“王𰉏曰：其隹（唯）丁冥（娩），嘉；其隹（唯）庚冥（娩），引吉。
# 驗辭：允，吉，不，

print("\n")
print(day + inquirer + "卜" + location + diviner + q2 + month + "    " + (day + inquirer + "卜" + location + diviner + q1 + month)[::-1])
print("\n")

