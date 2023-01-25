from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import requests
import time
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

# ========================================================================== drom parser
page = 1
headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 YaBrowser/22.11.5.715 Yowser/2.5 Safari/537.36"
}
count = 0
def info_in_json(count):
    car = {}
    car['Модель'] = model_car
    car['Двигатель'] = car_engine
    car['Год'] = year_car
    car['Цена'] = price_car
    car['Город'] = city_car
    car['Общие характеристики'] = filtered_info_car_arr
    car['Ссылка'] = link_card
    with open(f"{model_car}.json", "w", encoding="utf-8") as file:
        json.dump(car, file, ensure_ascii=False, indent=4)
        print(f"{car} машина создана {count}")
        print("==================================")

while True:
    
    if page == 1:
        url = "https://auto.drom.ru/volkswagen/"
    else: 
        url = f"https://auto.drom.ru/volkswagen/all/page{page}/"


    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "lxml")
        card_cars = soup.find_all("a", class_="css-xb5nz8 ewrty961")
        for item in card_cars:
            link_card = item['href']
            city_car = item.find('span', class_='css-1488ad e162wx9x0').text            
            model_car = item.find('span').text.split(', ')[0]
            year_car = item.find('span').text.split(', ')[1]
            info_car_arr = item.findAll('span', {'data-ftid': 'bull_description-item'})
            filtered_info_car_arr = []
            for item_info in info_car_arr:
                filtered_info_car_arr.append(item_info.get_text())
            car_engine = ""
            if item.find("div", class_="css-o2r31p e3f4v4l0") is not None:
                car_engine = item.find('div', class_='css-o2r31p e3f4v4l0').text
            price_car = item.find('span', {'data-ftid': 'bull_price'}).text
            count += 1
            info_in_json(count)
            time.sleep(5)
        page += 1
        print(f"{page}")
        time.sleep(3)
    else:
        break
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
