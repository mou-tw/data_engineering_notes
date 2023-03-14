### 選擇器
```
#元素
#批量的統一格式
ex:
p {color: "red";}

#ID
#i1 {
  background-color: red;
}

#class
#給某些特定標籤設定相同格式
.c1 {
  font-size: 14px;
}
p.c1 {
  color: red;
}


#後代選擇器
ex: li內部的a標籤的css
li a{
    color:red;
}

#父子選擇器
ex: 所有父級是div的p元素
div>p{
    color:red;
}

#鄰近選擇器
ex: 所有鄰近div之後的p元素，且必須是相同階級
div+p{
    color:red;
}
#兄弟選擇器
ex: li之後所有的兄弟p標籤
#li~p{
    color:red;
}

#自訂義屬性選擇器
[自訂義屬性] {
    color:red;
}

#混合使用
ex: id t1之後的臨近p元素
#t1+p{
    color:red;
}
ex: id t2之後的所有p元素
#t2~p{
    color:red;
}

```

### CSS優先級
```
當選擇器相同:
    越靠近標籤優先級越高

內聯   > id   > class > 基本元素選擇器
(1000)  (100)   (10)    (1)
相加不可進位

```

### CSS 偽類選擇器
```
# link was visitted
a:visited{}

# link被指標經過
a:hover{}
div:hover{}

#input focus模式(獲取到了滑鼠指標的閃爍狀態)
input:focus{}

```

### 偽元素選擇器
```
# 文字元素的第一個字
p:first-letter{}

```

### 字體相關屬性
```
#自型(按順序查找)
font-family
ex:
body {
  font-family: "Microsoft Yahei", "微软雅黑", "Arial", sans-serif
}
#字體大小
font-size
p{
    font-size:14px;
}

#自重(粗細)
font-weight
>> normal, bold, bolder, lighter, 100~900, inherit

#顏色
color
color:red
color:rgb(255,0,0)
color:rgb(255,0,0,0)
color:#00FF00

#文字對齊
text-align
>> left, right, center, justify(兩端對齊)

#文本裝飾
text-decoration
>> none, underline, overline, line-throught, inherit

#文本縮進
ex:
text:indent:28px

```

### 背景相關屬性
```
background-color
width
height
background-image:url("")
background-repeat: none/repeat-x, repeat-y
background-position: center/ [number] px [number] px, [0-100]%
background-attachment:fixed >>固定背景
```

### 邊框
```
border-width:10px
border-color:red
border-style:solid
>> border: 10px solid red

display
    >>inline(按照內容寬度展示)
    >>block(可設置list內的a標籤使整個block都能被點擊)
    >>inline-block
    
```
[display釋例](https://github.com/mou-tw/data_engineering_notes/blob/main/web_demos/display.html)

### CSS box
```
content
padding(內填充)
border(邊框)
margin(外邊框)
    >>auto居中

padding多用來調整內容區和邊框之間的距離
margin用以調整標籤與標籤之間的距離

```

### float and clear
```
div配合float作布局
float:left/right
設定float之後，所有元素都變成區塊標籤(不佔文檔位置)
搭配偽元素的clear屬性實現動態的div高度調整

clear 清除浮動的副作用(內容飛出，父標籤撐不起來)
clear:left(該元素的左邊不能有float元素)
配合偽元素來實現實現動態的div高度調整
.clearfix:after{
    content:"";
    display:block;
    clear:both
}
```
[float and clear釋例](https://github.com/mou-tw/data_engineering_notes/blob/main/web_demos/flaot_clear.html)

### overflow
```
overflow:
    >>auto 可調整框
    >>hidden 隱藏
    >>scroll 滾動條


```
### position
```
position:
    >>static(默認)
    >>relative(相對於原來的定位，搭配 top left等進行相對定位的調整)
    >>absolute(針對父標籤，搭配 top left等進行絕對定位的調整)
    >>fixed(永遠在畫面的某個位置)

float, absolute, fixes都會脫離文檔流

```

### opacity
```
    設置以調整透明度
    opacity>>元素和子元素的透明度效果
```

### z-index
```
針對定位過(position)的元素
設定前後順序

```


### tips
```
在一開始加入
*{
    border:0;
    margin:0;   
}
避免browser預設造成錯誤
```



* [reference1](https://www.cnblogs.com/liwenzhou/p/7999532.html)
* [reference2](https://developer.mozilla.org/zh-CN/docs/Web/CSS/Descendant_combinator)

