from bs4 import BeautifulSoup
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

# ==========================================================================

# x = int(input("Введите размерность массива по столбцам: ")) # 5
# y = int(input("Введите размерность массива по строкам: ")) # 3
# x, y = [int(item) for item in input("Введите размерность массива(первое значение-количество столбцов) через проблел: ").split()]

x, y = map(int, input().split())
count = 1
arr = [[0] * x for i in range(y)]
for i in range(0, len(arr)):
    for j in range(0, len(arr[i])):
        arr[i][j] = count
        print(arr[i][j], end="  ") if (count < 10) else print(arr[i][j], end=" ")
        count += 1
    print("", end="\n")
