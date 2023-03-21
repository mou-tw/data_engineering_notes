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

```




