import requests
from bs4 import BeautifulSoup
import time
import json

api_url = 'https://ani.gamer.com.tw/animeList.php'

headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64;x64) AppleWebKit/537.36 (KHTML,    like Gecko) Chrome142.0.0.0 Safari/537.36' ,
}

page = 1
adventure_animation_list = []

while True:
    params = {
        'tags': '冒險',
        'page': page,
    }    


    req = requests.get(api_url , headers=headers , params=params)
    if req.status_code == 200:
        print(f'請求成功:第{page}頁')
        
        soup = BeautifulSoup(req.text, 'html.parser')

        main = soup.select('.theme-list-main')
        if not main:
            print('已無資料')
            break

        for anime_item in main:
            # 標題
            anime_name = anime_item.select_one('p.theme-name').text.strip()
            # 年份
            anime_time = anime_item.select_one('p.theme-time').text.strip().replace('年份：',   '')
            # 集數
            anime_number = anime_item.select_one('span.theme-number').text.strip()
            # 觀看數
            anime_view_number = anime_item.select_one('.show-view-number > p').text.strip()
            # 封面
            anime_image_tag = anime_item.select_one('img.theme-img')
            anime_image = anime_image_tag.get('data-src') or anime_image_tag.get('src')


            anime_data = {
                "title": anime_name,
                "year": anime_time,
                "theme": anime_number,
                "view": anime_view_number,
                "cover": anime_image
            }
            
            adventure_animation_list.append(anime_data)
            
        page += 1
        time.sleep(1)

    else:
        print(f'請求失敗:{req.status_code}')
        break
with open('adventure_animation_list(en).json','w' ,encoding='utf-8') as file:
    json.dump(adventure_animation_list, file, ensure_ascii=False, indent=4)
print(f'資料存取結束!! 共{len(adventure_animation_list)}筆資料')