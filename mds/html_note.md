## html notes


```
#常用標籤
<b>加粗</b>
<i>斜體</i>
<u>下底線</u>
<s>刪除</s>

<p>段落标签</p>
#換行
<br>
#水平線
<hr>

#div and span
#沒有自有默認特性，可透過css 改動div 和span
#div
#span
<div>自行一行，默認占browser寬度</div>
<span>由內容決定長度</span>

```

### 元素分類
```
#區塊元素(block)標籤
    默認占browser寬度，可設置長寬
    h1-h6 div p hr
#行內元素(inline)標籤
    大小根據內容決定，不能設置長寬
    a img u s i b span

#行內標籤不能嵌套區塊標籤
#p標籤不能嵌套區塊標籤
```


### html list tag
```
#order
<ol type> </ol>

    #type 屬性
        1(數字列表)
        A(大寫字母) 
        a(小寫字母)
        I(大寫羅馬)
        i(小寫羅馬) 
    #start開始順序
#unorder
<ul type> </ul>

    #type 屬性
        disc（默認，圓點）
        circle（空心圓）
        square（方塊）
        none(無樣式)

#階層(標題)列表
<dl>
    <dt>標題1</dt>
    <dd>內容1.1</dd>
    <dt>標題2</dt>
    <dd>內容2.1</dd>
    <dd>內容2.2</dd>
</dl>

```
### table format
```
<table>
    <thead  >
    <tr>
        <th>col1</th> --> column name1
        <th>col2</th> --> column name1
        <th>col3</th> --> column name1
    </tr>
    </thead>
    <tbody>
    <tr> --> first row
        <td>>1</td>
        <td>>2</td>
        <td>>3</td>
    </tr>
    <tr> --> second row
        <td>>1</td>
        <td>>2</td>
        <td>>3</td>
    </tr>
    
    </tbody>

</table>

thead 參數

```

### 快速指令
```
h1*4>a.c1[id=a$]{atag$}

>>
<h1><a href="" class="c1" id="a1">atag1</a></h1>
<h1><a href="" class="c1" id="a2">atag2</a></h1>
<h1><a href="" class="c1" id="a3">atag3</a></h1>
<h1><a href="" class="c1" id="a4">atag4</a></h1>

#format code
Alt + Shift +F
#嵌套
Alt +W

```

### form
```
#前後端數據交流的時候使用form

#action參數
    往哪個url提交
#method參數
    GET POST
#enctype參數
    enctype="multipart/form-data"
    必須輸入後端才能收到文件
#autocomplete
    自動補全
#novalidate
    檢查如email的格式

```


### input
```
#checked參數
#readonly參數
#value參數
    默認值
#placeholder
    默認顯示

text
password
radio 單選
checkbox 多選
date 日期
datetime 時間
file 文件(上傳文件，form標籤寫一個特殊屬性enctype)
button 普通botton，多用JS綁定事件
reset 
submit

```

### select 下拉菜單
```
optgroup 分組的下拉選單
option 具體的下拉選項

```


### label 標籤
```
透過label標籤，可實現按文字等同點擊框
```

[reference](https://www.cnblogs.com/liwenzhou/p/7988087.html)