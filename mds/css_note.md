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
    >>block()
```

### CSS box
```



```


* [reference1](https://www.cnblogs.com/liwenzhou/p/7999532.html)
* [reference2](https://developer.mozilla.org/zh-CN/docs/Web/CSS/Descendant_combinator)

