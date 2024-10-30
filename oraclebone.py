import numpy as np
import random
import time
from datetime import datetime, timedelta
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
    return cnmonth[month - 1] + "月"
# ------ main ------
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

inquirer = str(input("Inquirer name (optional): "))
location = str(input("Location (optional): "))
diviner = str(input("Diviner name: "))

q1 = str(input("The question: "))

# time.sleep(1)
# print("Calculating...")
# time.sleep(5)

inquirer = inquirer[0] if inquirer else ""
location = ("才" + location[0]) if location else ""
diviner = diviner[0] + "貞"
month = month + "月"

print(day + inquirer + "卜" + location + diviner + "[命辭]" + month)