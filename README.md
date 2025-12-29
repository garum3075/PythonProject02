## 使用巴哈姆特動畫瘋冒險類動畫的資料進行爬蟲 /<br>運用python和pandas進行資料處理

### AdventureAnimation.py /<br>adventure_animation_list.json / adventure_animation_list(en).json
<table>
    <thead>
        <tr>
            <th width="80px">編號</th>
            <th width="150px">學習目標</th>
            <th width="100px">狀態/備註</th>
            <th width="450px">遇到問題與解決方案</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td align="center">01</td>
            <td>
                使用BeautifulSoup進行爬蟲
            </td>
            <td align="center">✅</td>
            <td>
                1. 無法正確取得資料(取得資料為空白)<br>
                解決方法<br>
                (1) 反覆確認使用區塊<br>
                (2) 確認區塊無誤後檢查程式碼問題<br>
                (3) 隨時都print資料確認資料錯誤的點<br>
            </td>
        </tr>
        <tr>
            <td align="center">02</td>
            <td>
                學會使用select/selectone去取得資料
            </td>
            <td align="center">✅</td>
            <td>-</td>
        </tr>
        <tr>
            <td align="center">03</td>
            <td>
                使用json.dump匯出json檔(中、英各1)
            </td>
            <td align="center">✅</td>
            <td>-</td>
        </tr>
    </tbody>
</table>

### AdventureAnimation.html
<table>
    <thead>
        <tr>
            <th width="80px">編號</th>
            <th width="150px">學習目標</th>
            <th width="100px">狀態/備註</th>
            <th width="450px">遇到問題與解決方案</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td align="center">01</td>
            <td>
                進行資料重構
            </td>
            <td align="center">✅</td>
            <td>
                1. 無法正確資料重構<br>
                解決方法<br>
                (1) 將過往上課使用的程式碼和現在的程式碼給Gemini去確認哪裡不同。Gemini答非所問，所以改成詢問錯誤代碼內容。<br>
                (2) 反覆確認後發現 80行AdventureAnimationData 打成 animationData
            </td>
        </tr>
        <tr>
            <td align="center">02</td>
            <td>
                使用 Chartjs進行表格製作
            </td>
            <td align="center">✅</td>
            <td>
                1. 近年動畫名稱過長，會影響Chartjs外觀<br>
                解決方法<br>
                (1) 將文字改成圖檔的方式<br>
                (2) 因為各月份動畫數量不同，進行調整圖檔大小<br>
                <br>
                2. Chartjs X軸無法正常顯示想要的數據<br>
                解決方法<br>
                (1) 確認Chartjs X軸無法判別「164萬」是什麼文字<br>
                (2) 使用replace將'萬'改成''，並在標題上補上單位<br>
                <br>
                3. 經過第2點後發現資料處理繁瑣，上網後發現資料都要進行清洗，所以就暫停Chartjs的使用並開始進行資料清洗
            </td>
        </tr>
    </tbody>
</table>
