bootstrap file structure
```
-css //css文件
    -xxxx.css.map //壓縮對應文件
    -xxxx.min.css //壓縮文件
    -xxxx.min.css.map //壓縮對應文件
-fonts //字體文件

-js 

```


tag

```
#移動設備尺寸優先
<meta name="viewport" content="width=device-width, initial-scale=1">
#統一不同瀏覽器之間的初始狀態
<link href="https://cdn.bootcdn.net/ajax/libs/normalize/8.0.1/normalize.css" rel="stylesheet">

```
* [bootcdn](https://www.bootcdn.cn/)


class (grid)
```
div class
container 
    row (由12個col單位組成，必須放在container class中，超過12col會換一個row)
        col-md-1 //佔 1/12個row(在PC端 or中等螢幕 >=992px)
        col-md-10 //佔 10/12個row(在PC端)
        col-sm-1 //佔 1/12個row(在移動端-小尺寸 >=768px)
        col-xs-1 //佔 1/12個row(在移動端-超小尺寸 <768px>)
        col-lg-1 //佔 1/12個row(在移動端-超大尺寸 >=1200px)
        col-md-offset-2 //左邊空出two columns
        col-md-push-3 //向右推3個col
        col-md-pull-3 //向左推3個col

lead //文字加粗提示
<mark> //提示高亮度
<del> //刪除
<s    //無用文本
<ins> //下底線
<u>   //下底線文本
<small> // 小號
<strong> //粗體
<em> //斜體
<adress> //聯絡訊息相關

```

class text
```
class='text-left'
class='text-center'
class='text-right'
class='text-justify'
class='text-nowrap'
class='text-lowercase'
class='text-uppercase'
class='text-capitalize'//首字大寫
 
```

abbr title
```
<abbr title='attribute'> //懸浮停頓產生title內容
<abbr title='attribute' class='initialism'> // 用於首字母縮寫，如HTML

```

引用
```
<figure>
    <blockquote class="blockquote">
        <p>some famoue quote</p>
    </blockquote>
    <figcaption class="blockquote-footer">
        Someone famous in <cite title="Soure Title">Some Article</cite>
    </figcaption>
</figure>
 
>>
 some famous quote
    -- Someone famoue in Some Article


```

內聯(橫向排列)的list

```
    <ul class="list-inline">
        <li class="list-inline-item">1</li>
        <li class="list-inline-item">2</li>
        <li class="list-inline-item">3</li>
    </ul>

```

描述的短語列表
```

<dl>
    <dt>123</dt>
    <dd>sasdqwdcasdfasdfasdf</dd>
    <dt>456</dt>
    <dd>sasdqwdcasdfasdfasdf</dd>
</dl>

dl class='dl-horizontal' //橫向表示法

```

顯示html標籤
```
<code>$lt;div$gt; </code>

多行代碼
<pre>

```

others
```
<kbd></kbd> //模擬鍵盤
<var> //變量(公式)
<samp> //標記程式輸出的內容
```

table 
```
table class =
table //bootstrap表格形式
table-bordered  //邊框
table-striped   //隔行變色
table-hover     //滑鼠懸停變色
table-condensed //縮小表格

table row 變色
tr class=
table-warning
table-danger
table-primary......

RWD table
div class = 'table-responsive'

```


media
```
取得瀏覽器設備的相關訊息

```

box-sizing
```
bootstrap5 預設是border-box
border-box會以整個border作為width
調整padding會自動往內縮
margin則為往外加

content-box則否，以content為中心
任何的margin和padding皆為另計

```