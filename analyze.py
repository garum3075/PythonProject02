import json
with open('adventure_animation_list(en).json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# 進行資料清洗
import pandas as pd
DF = pd.DataFrame(data)
# view 清洗成 view_num
def parse_view(view):
    try:
        return int(float(view.replace("萬", "")) * 10000)
    except:
        return None
DF['view_num'] = DF['view'].apply(parse_view).astype('Int64')

# theme 清洗成 episodes
def parse_episodes(theme):
    try:
        num = theme.replace('共' , '').replace('集' , '')
        return int(num)
    except:
        return None
DF['episodes'] = DF['theme'].apply(parse_episodes)

# year/month 分開清洗成 release_year 和 release_month
def parse_year_month(year_str):
    try:
        year , month = year_str.split('/')
        return int(year) , int(month)
    except:
        return None , None
DF[['release_year' , 'release_month']] = DF['year'].apply(parse_year_month).apply(pd.Series)

DF["release_year"] = DF["release_year"].astype("Int64")
DF["release_month"] = DF["release_month"].astype("Int64")


# ==================== 年排前3 ====================
# 清除缺失值
DF_rank = DF.dropna(subset = ['release_year' , 'release_month'])
# 排序
DF_rank = DF_rank.sort_values(by = ['release_year' , 'view_num'] , ascending = [True , False])

top3_by_year = (
    # 取前三
    DF_rank.groupby('release_year').head(3)
    # 重新排序
            .reset_index(drop = True)
)
# 年份 標題 觀看數
top3_by_year = top3_by_year[['release_year' , 'title' , 'view_num']]

# ==================== 取5年 ====================
# release_year 最大值
latest_year = DF['release_year'].max()

DF_5year = DF[( DF['release_year'] >= latest_year-4)]
DF_5year_month = DF_5year.dropna( subset = ['release_year' , 'release_month' , 'view_num'])
DF_5year_month = DF_5year_month.sort_values( by = ['release_year' , 'release_month' , 'view_num'] , ascending = [True , True , False])

# ==================== 5年內年排前3 ====================
top3_by_year_5y = (
    DF_5year.groupby(['release_year']).head(3)
            .reset_index(drop = True)
)
top3_by_year_5y = top3_by_year_5y[['release_year' , 'release_month' , 'title' , 'view_num' , 'cover']]

# print('檢查', top3_by_year_5y)

# 匯出csv
# top3_by_year_5y.to_csv('top3_by_year_5y.csv', index=False, encoding='utf-8-sig')


# import pandas as pd
# import matplotlib.pyplot as plt
# from matplotlib.offsetbox import OffsetImage, AnnotationBbox
# import requests
# from io import BytesIO
# from matplotlib.ticker import ScalarFormatter

# # 中文顯示
# plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 

# def get_image(url):
#     """使用 requests 抓取圖片"""
#     try:
#         headers = {'User-Agent': 'Mozilla/5.0'}
#         response = requests.get(url, headers=headers, timeout=10)
        
#         # 檢查請求是否成功
#         response.raise_for_status() 
        
#         # BytesIO
#         image_data = BytesIO(response.content)
#         return plt.imread(image_data, format='JPG')
        
#     except Exception as e:
#         print(f"圖片下載失敗: {url}，原因: {e}")
#         return None

# # 拿出2025-2021年度
# years = sorted(top3_by_year_5y['release_year'].unique(), reverse=True)

# for year in years:
#     year_data = top3_by_year_5y[top3_by_year_5y['release_year'] == year].copy()
#     # 由高到低
#     year_data = year_data.sort_values('view_num', ascending=True)
    
#     # 建立畫布
#     fig, ax = plt.subplots(figsize=(12, 6))
    
#     # 繪製長條圖
#     bars = ax.barh(
#         year_data['title'],
#         year_data['view_num'],
#         color='skyblue',
#         edgecolor='navy',
#         alpha=0.8
#         )
    
#     # 解決科學記號問題
#     ax.xaxis.set_major_formatter(ScalarFormatter(useOffset=False))
#     # 強制顯示為一般數字
#     ax.ticklabel_format(style='plain', axis='x')
    
#     # 處理左側圖片標籤
#     # 給索引
#     for i, (idx, row) in enumerate(year_data.iterrows()):
#         img = get_image(row['cover'])
#         if img is not None:
#             # 調整圖片大小
#             imagebox = OffsetImage(img, zoom=0.25) 
#             ab = AnnotationBbox(imagebox, (0, i),
#                                 xybox=(-60, 0), 
#                                 xycoords='data',
#                                 boxcoords="offset points",
#                                 frameon=False)
#             ax.add_artist(ab)
            
#         # 標註觀看數
#         ax.text(row['view_num'], i,
#                 f"{ int(row['view_num']):,}", 
#                 va='center',
#                 fontsize=12,
#                 fontweight='bold',
#                 color='darkblue'
#         )

#     # 圖表細節
#     ax.set_title(
#         f'【{year} 年度】巴哈姆特冒險類動畫 - 觀看數前三名',
#         fontsize=20, pad=30
#     )

#     ax.set_xlabel(
#         '總觀看次數',
#         fontsize=14
#     )
    
#     # 隱藏文字標題
#     ax.set_yticklabels([]) 
    
#     # 增加邊界，確保圖片與數值不會被切掉
#     plt.subplots_adjust(left=0.25, right=0.9)
#     plt.tight_layout()
    
#     file_name = f'bahamut_top3_{year}.png'
#     fig.savefig(file_name, dpi=300, bbox_inches='tight')
    
#     print(f'已成功匯出：{file_name}')

#     plt.show()