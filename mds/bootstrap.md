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


```

media
```
取得瀏覽器設備的相關訊息

```