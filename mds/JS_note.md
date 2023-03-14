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
>>>第一步會先實例Active Object(AO)
>>>如局部變量有值，不做任何操作，如沒有變量賦值給，且值為undefined
>>>函數聲明，如果AO有則將其覆蓋，如果沒有則不做動作
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

