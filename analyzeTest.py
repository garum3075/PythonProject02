import json
with open('adventure_animation_list(en).json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# print('檢查1',type(data))
# print('檢查2',len(data))
# print('檢查3',data[0])

import pandas as pd
# DataFrame
DF = pd.DataFrame(data)
# print('檢查4',DF.head())

# print('檢查5',DF.dtypes)

# print('檢查6', DF['view'].head(10))

def parse_view(view):
    try:
        return int(float(view.replace("萬", "")) * 10000)
    except:
        return None
DF['view_num'] = DF['view'].apply(parse_view).astype('Int64')

# print('檢查7' , DF[['view' , 'view_num']].head())
# print('檢查8' , DF.dtypes)
# print('檢查9' , DF['theme'].head(10))

def parse_episodes(theme):
    try:
        num = theme.replace('共' , '').replace('集' , '')
        return int(num) # 目的：讓字串好看
    except:
        return None

DF['episodes'] = DF['theme'].apply(parse_episodes)

# print('檢查10' , DF[['theme' , 'episodes']].head(10))
# print('檢查11' , DF.dtypes)

# print('檢查12' , DF["year"].head(10))

def parse_year_month(year_str):
    try:
        year , month = year_str.split('/')
        return int(year) , int(month)
    except:
        return None , None
DF[['release_year' , 'release_month']] = DF['year'].apply(parse_year_month).apply(pd.Series)

DF["release_year"] = DF["release_year"].astype("Int64")
DF["release_month"] = DF["release_month"].astype("Int64")

# print('檢查13' , DF[["year", "release_year", "release_month"]].head(10))
# print('檢查14' , DF.dtypes)

# print('檢查15' , DF["release_year"].isnull().sum())
# print('檢查16' , DF["release_month"].isnull().sum())




DF_rank = DF.dropna(subset = ['release_year' , 'release_month'])
DF_rank = DF_rank.sort_values(by = ['release_year' , 'view_num'] , ascending = [True , False])
top3_by_year = (DF_rank.groupby('release_year').head(3).reset_index(drop = True))
# groupby("release_year") → 分年
# head(3) → 每組取前三筆（因為已排序）
# reset_index() → 表格比較乾淨
# print('檢查17' , top3_by_year)

# 留下 年份 標題 觀看數
top3_by_year = top3_by_year[['release_year' , 'title' , 'view_num']]
# print('檢查18' , top3_by_year.head(10))

DF_month = DF.dropna(subset = ['release_year' , 'release_month' , 'view_num'])
DF_month = DF_month.sort_values(by = ['release_year' , 'release_month' , 'view_num'] , ascending = [True , True , False])

latest_5year = DF['release_year'].max()
# print('檢查19' , latest_5year)

DF_5year = DF[( DF['release_year'] >= latest_5year-4)]
DF_5year_month = DF_5year.dropna( subset = ['release_year' , 'release_month' , 'view_num'])
DF_5year_month = DF_5year_month.sort_values( by = ['release_year' , 'release_month' , 'view_num'] , ascending = [True , True , False])

# 取前三名 / Excel產出
top3_by_month_5y = (DF_5year_month.groupby(['release_year' , 'release_month']).head(3).reset_index(drop = True))

top3_by_month_5y = top3_by_month_5y[['release_year' , 'release_month' , 'title' , 'view_num']]

# print('檢查20' , top3_by_month_5y.head(50))


# Excel產出
# top3_by_month_5y.to_excel('top3_by_month_last5years.xlsx' , index = False)

top3_by_year_month = (DF_5year.dropna(subset = ['release_year' , 'release_month' , 'view_num']).sort_values(by = ['release_year' , 'release_month' , 'view_num'] , ascending = [True , True , False]).groupby(['release_year' , 'release_month']).head(3))

# 產圖B 2021–2025 各月份 Top 3（每一年 × 每一月，各自一張 bar 圖）

# import matplotlib.pyplot as plt
# import matplotlib.image as mpimg
# from matplotlib.ticker import FuncFormatter
# from io import BytesIO
# import requests
# from PIL import Image
# import numpy as np

# plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
# plt.rcParams['axes.unicode_minus'] = False

# def format_wan(x, pos):
#     return f'{int(x/10000)}萬'

# for (year, month), group in top3_by_year_month.groupby(
#         ['release_year', 'release_month']
#     ):

#     fig, ax = plt.subplots(figsize=(8, 6))
#     num_bars = len(group)

#     if num_bars == 1:
#         xAxis = [1]
#     else:
#         xAxis = np.linspace(0, 2, num_bars)

#     print("****************************")
#     print(xAxis, xAxis.__class__)
#     print(group['view_num'])

#     ax.bar(xAxis, group['view_num'], width=0.5, zorder=2)

#     max_view = group['view_num'].max()
#     ax.set_ylim(-max_view * 0.25, max_view * 1.1)
#     ax.set_xlim(-0.5, 2.5)
#     ax.set_xticks([])

#     for i, url in enumerate(group['cover']):
#         try:
#             response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})

#             img = Image.open(BytesIO(response.content))
#             img = np.array(img)

#             ax.imshow(
#                 img,
#                 extent=(i-0.3, i+0.3, -max_view*0.5 , -max_view*0.01),
#                 aspect='auto',
#                 zorder=5,
#                 clip_on=False
#             )

#         except Exception as e:
#             print("圖片讀取失敗：", url, e)

#     ax.set_title(f'{year} 年 {month} 月 TOP 3 動畫')
#     ax.set_ylabel('觀看數')
#     ax.set_ylim(0, max_view * 1.1)

#     ax.ticklabel_format(style='plain', axis='y')
#     ax.yaxis.set_major_formatter(FuncFormatter(format_wan))

#     plt.tight_layout()
#     plt.show()