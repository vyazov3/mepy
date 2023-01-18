from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import requests
import json
import os

# url = "https://health-diet.ru/table_calorie/"

# headers = {
#     "Accept": "*/*",
#     "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 YaBrowser/22.11.5.715 Yowser/2.5 Safari/537.36"
# }

# r = requests.get(url, headers = headers)

# soup = BeautifulSoup(r.text, "lxml")
# types_food = soup.find_all("a", class_="mzr-tc-group-item-href")

# categories = {}

# for item in types_food:
#     text_item = item.text
#     link_item = "https://health-diet.ru" + item.get("href")
#     categories[text_item] = link_item

# for category, link in categories.items():  
#     rep = [", "," ", ",", "-", "'"]
#     for item3 in rep:
#         if (item3 in category):
#             category = category.replace(item3, "_")
#     with open(f"{category}.json", "w", encoding="utf-8") as file:
#         json.dump(categories, file, ensure_ascii=False, indent=4)

# ========================================================================== avito parser
url = "https://www.avito.ru/lipetsk/avtomobili/volkswagen/golf-ASgBAgICAkTgtg24mSjitg3Ipig?cd=1&radius=200"

# headers = {
#     "Accept": "*/*",
#     "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 YaBrowser/22.11.5.715 Yowser/2.5 Safari/537.36",
#  }

response = requests.get(url, headers={'User-Agent': UserAgent().chrome})
for key, value in response.request.headers.items():
    print(key+": "+value)
print(requests.get(url))



# ========================================================================== the task
# x = int(input("Введите размерность массива по столбцам: ")) # 5
# y = int(input("Введите размерность массива по строкам: ")) # 3
# x, y = [int(item) for item in input("Введите размерность массива(первое значение-количество столбцов) через проблел: ").split()]


# 1  2  3  4  5
# 16 17 18 19 6
# 15 24 24 20 7
# 14 23 22 21 8
# 13 12 11 10 9
# x, y = map(int, input().split())
# count = 1
# direction = 0;
# arr = [[0] * x for i in range(y)]
# for i in range(0, len(arr)):
#     if (direction == 0):
#         for j in range(0, len(arr[i])):
#             arr[i][j] = count
#             print(arr[i][j], end="  ") if (count < 10) else print(arr[i][j], end=" ")
#             count += 1
#         direction += 1
#     if (direction == 2):
#         print(i)
#     print("", end="\n")
