所有和html文件相關的參數都放在settings.py

要獲取的標籤必須放在form表單中，且標籤都要有name屬性
action屬性控制往哪個地方(url/function)提交,method一般為post
提交按鈕為 submit button


Django 
>> project 項目(momo)
>> app 應用模塊(筆電館)


add app in Django
>> in project root path
>> python manage.py startapp [app name]
>> 在 project root path 底下會新增一個 [app name] 的資料夾
>> 其中 apps.py(app相關設定), views.py(function page), models.py, tests.py(寫測試)
>> 在settings.py中的 INSTALLED_APPS新增 '[app name].apps.Config'