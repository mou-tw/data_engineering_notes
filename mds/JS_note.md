DOM(Document object model)
>>整合js, css, html
BOM(Browser object model)
>>整合JS與瀏覽器


立即執行函數(保護變數不會汙染全局變量)
```
(function foo(a,b) {
    console.log(a);
    console.log(b);
    var c = a+b;
    console.log(c);
})(11,22)

console.log(c) >> c is not defined
```


argumnts(取得所有函數的input參數)
```
function func1(a,b) {
    console.log(a);
    console.log(b);
    console.log(arguments.length);
    for (var i =0; i<arguments.length; i++){
        console.log(arguments[i]);
    }
}

```

詞法分析
1. 第一步會先實例Active Object(AO)
2. 如局部變量有值，不做任何操作，如沒有變量賦值給，且值為undefined
3. 函數聲明，如果AO有則將其覆蓋，如果沒有則不做動作
```
var age=18;
function foo(){
    console.log(age);
    var age = 22;
    console.log(age);
    function age(){
        console.log("inner")
    }
    console.log(age);
}

foo()

>>function....
>>22
>>22

```

JS的dictionary
```
遍歷JS的dictionary
JS dictionary的key 默認不用加""
var dict = {"a":"asdf", "b":"xzxcv"}
等同
var dict = {a:"asdf", b:"xzxcv"}

for (var i in dict){
    console.log(i)
    console.log(dict[i)
}
```

JS的內製date module
```
var dt = Date(0)
var dt = new Date()
var dt_str = dt.toLocalString()

```


window function
```
alert >> 彈出視窗
等同window.alert
confirm >>彈出是否視窗
prompt >> 彈出文字輸入視窗

```

計時相關
```
setTimeout()
幾毫秒後執行
ex:1秒後彈出視窗
var t = setTimeout("alert(123);",1000);
ex:5秒後執行特定function
var t = setTimeout(foo,5000);
clearTimeout([輸入setTimeout 返回的數字])

setInterval()
每個幾毫秒執行
var t = setInterval(foo,5000);
clearInterval(t)

```



DOM tree
```
document    
    >>html
        >>element(head)
            >>title
                >>text
        >>element(body)
            >>h1
            >>a  (attribute) .....
                >>text
document代表整個文檔
element代表一個元素(標籤)
text代表元素中的文本
attribute 代表一個屬性，element有屬性

```

JS操作DOM
```
<查找>
document.getElementById()
document.getElementByClassName()
document.getElementByTagName()

找父標籤
parentElement
找子標籤
children
firstElementChild
lastElementChild
nextElementSibling
previousElementSibling

<創建>
createElement, createTextNode
>>appendChild
>>insertChild
>>insertBefore(內容,位置  )

ex:
var crtEle = document.createElement("img")
crtEle.src = "....."
var t = document.getElementById("")
t.appendChild(crtEle)

ex:
var crtEle = document.createElement("div")
var contentText = document.createTextNode("text...")
crtEle.appendChild(contentText)
var i1Ele = document.getElementById("i1")
i1Ele.appendChild(crtEle)
```

JS_event
```
onclick
ondbclick
onfucus(click搜尋框)
onblur(從搜尋眶離開，點擊其他處)
onchange(域的內容發生改變，常用於下拉選單內容發生改變觸發)


```

this的理解
event內的this指的是event發生的'標籤'