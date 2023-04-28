JQUERY需先導入，在script標籤之前先引入

* [cheat sheet](https://oscarotero.com/jquery/)

導入方法
```
<script src=""jquery-3.x.x.min.js"></script>
```
選擇器
```
#id 
$("#")
#class
$(".")
#混合
$("xx,xx")
#level
$("x>y")
#所有後代
$("x>y")
#next
$("x+y")
#以後所有
$("x~y")
#屬性
$("input:text")
$("input[name='xxx']")
表單對象屬性
:enable
:disable
:checked
:selected

```

JQuery object vs JS object
```
#JQuery object
var $Ele = $(Ele)

#JQuery to DOM
document.getElementId('p')
$("p")[0]

#DOM to JQuery
var pEle = document.getElementById("p")
$(pEle)
```
篩選
```
:first
:last
:eq(index)
:odd &:even >>用於表格變色
:gt(index)
:index
:not()
:has()
ex: 
in html
<div>
<div class="c"> <a></div>
</div>
$("div .c:has('a')")

表單常用篩選
:text
:password
:file
:radio
:checkbox
:submit
:reset
:button
ex: find all checkbox
$(":checkbox")

#下一個
$()\
.next() >> 下一個
.nextAll() >> 下一個以後所有
.nextUntil() >> 下一個直到
.prev() >>上一個
.prevAll() >> 上一個以前所有 
.prevUntil() >> 上一個直到
.parent() >>找父標籤
.parents() >>找所有父標籤
.parentsUntil()>>找所有當前元素的父標籤，直到匹配為止
.children() >>子級
.siblings() >>兄弟
.find()
```

操作class
```

$()\
.addClass();
.removeClass();
.hasClass()
.toggleClass()
click


```
操作css
```
$(JQ object).css

```

## object size

```
$().height()
    >>content height
$().width()
    >>content height
$().innerHeight()
    >>content+padding height
$().innerWidth()
    >>content+padding width
$().outerHeight()
    >>content+padding+border height
$().outerWidth()
    >>content+padding+border width
```

## Modify Html
```
$().text('修改標籤text')
$().html('修改標籤整體內容')
    ex:
        $().html("<a src='http://......'>demo</a>")

```

## JQuery vs DOM
```
$().html()
    == .innerHtml
$().text()
    == .innerText

屬性操作

.attr(
    attrName 返回第一個符合的屬性值
    attrName, attrValue 為所有元素設置一個屬性值
    {k1:v1,k2:v2}為所有匹配元素設置多個屬性值
)
removeAttr()
```
prop
```
$().prop(
    attrName,
    Boolen
)
ex:
$('.i1').prop('check',false)

使用於檢查checkbox或者radio是否被選中，返回booeln值


```

val
```
得到用戶輸入值

```

文檔處理
```
$(A).append(B) //把B追加到A最後面
$(A).appendTo(B) //把A追加到B最後面

$(A).prepend(B) //把B追加到A最前面
$(A).prependTo(B) //把A追加到B最前面

$(A).after(B) //把B放到A之後
$(A).InsertAfter(B) //把A放到B之後

```


on
```
使用on來取代click等的事件

$().on("click), function(){})
$().on("click), "選擇器",function(){})
使合用於給未來的element，或者冒泡事件，由於在頁面再生成時還沒有產生
無法用原先JQUERY 事件執行

```

return false & break
```
多個事件之間，如果需要阻止後續事件的執行
    >> retrun false
退出循環
    >> break

```

鍵盤相關事件
```
keydown
keyup
ex: $('body).on('keydown',function(){event})
將鍵盤按下時的事件作為參數傳遞
查看按鍵event.keyCode

```

確保綁定事件時DOM樹是完成的
```
$(document).ready(function({
    .......
}))
等同
$(function(){
    .....
})()

```
JQuery 動畫

```
show(time[毫秒])
hide()
toggle()

#滑動
slideDown()展開
slideUp()收起
slideToggle()

#淡入淡出
fadeIn(time,透明度)淡入
fadeOut()淡出
fadeTo()淡出至 

``` 

JQuery each loop
```
$().each(
    function(){.....}
   
)

function 內部的this是一個DOM object
function  可透過return false中斷循環,return 跳過當次循環 

.each(可迭代對象, function(.....){.....})
ex:
    var a1 = [11,22,33,44];
    $.each(a1, function(k,v){
        console.log(k+":"+v)
    })
    >>
    0:11
    1:22
    2:33
    3:44 


```

JQuery data
```
.data 類似python dictionary
ex:
    $().data('k',"v")
    $().data('k') >> "v"
    var $imgEle = $('img')
    $().data('img',$imgEle)
    $().data('img').attr('src','')

```

Ajax
```
$.ajax({
  url:,
  method:,
  dataType:,
  data:
  
  success:function(res){console.log(res)},
  error:function(err){console.log(err)},
});
```

* [解決CORS問題](https://ithelp.ithome.com.tw/articles/10268821)