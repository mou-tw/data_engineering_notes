DAX
可建立
1. Measure(使用時才做計算)
2. column(計算起來放，太多會影響效能)
3. table


create caculation groups
意圖解決Measure過多情況下效能受影響問題
需安裝tabular editor


```
SUMX()
類似excel的sumif

Caculate(expression, filter content)
固定特定意圖，並取得此計算結果

RELATED()
協助取用和自身關聯表內的數據

ex:
sales non USA = sumx(
    filter (sales, related(' Sales Territory'[Country]) <> "US"),
    Sales[Sales Amount]
)

USERELATIONSHIP
ex:
把SALES表的shipdatekey 和date(ROLE PLAYING DIMENTION TAB) Datekey連接起來
而不是原始的連接
salses by shipping date = caculate(
    SUM( Sales[Sales Amount]),
    USERELATIONSHIP( Sales[ShipDateKey], "Date"[DateKey])
)

CROSSFILTER
雙向作用性
ex:
想要用日期維度表資訊，篩選銷售資訊，顯示商品狀況

Number of products sold = CACULATE(
    DISTINCTCOUNT('Product'[ProductKey]),
    CROSSFILTER(Sales[ProductKey], Product[ProductKey], Both)
)

COMBINEVALUES
將兩個string合併成一個新的string column

TREATAS

假設資料顆粒度(granularity)不同，想要建立虛擬關聯
ex:

將advertising year和advertising month number與summarize 
Date表中的year和 Month Number做關聯

Total Advertising = CACULATE(
    SUM(Advertising[AdvertiseAmount],
    TREATEAS(
        SUMMARIZE('Date','Date[Year],'Date'[MonthNumber]),
        Advertising[Year],
        Advertising[Month Number]
    )

    )
)

Parent adn child function
PATH
把父子階層關係拆解出來

PATHITEM
把PATH關係的層級關係取出，搭配LOOKUPVALUE取直




Security

RLS row level security
    restrict access to PBI

    define dynamic rules
        DAX - userprincipalname

OLS object-level sucurity
object可能是column or tables
OLS 和RLS不能並存
需要透過Tabular Editor
https://github.com/MicrosoftLearning/DP-500-Azure-Data-Analyst.zh-cn




optimize PBI perfomance
DAX Studio

from 
    data source
    data model >> 越小越好
    visualizations
    environment >>機器效能、網路等

import , directQuery, Dual
import 透過vertiPaq壓縮暫存在Memory
directQuery 需要和來源取
使用Dual模式使PBI自行判斷資料表的讀取模式效能和者最好



BPA Best Practice Rules 原則
一個JSON 定義原則
https://github.com/microsoft/Analysis-Services/tree/master/BestPracticeRules
```