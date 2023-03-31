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


```