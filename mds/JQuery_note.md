JQUERY需先導入，在script標籤之前先引入
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

操作樣式
```
下一個
$()\
.addClass();
.removeClass();
.hasClass()
.toggleClass()

```

屬性操作
```
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

$(A).before(B) //把B放到A之前
$(A).InsertBeofre(B) //把A放到B之前
```