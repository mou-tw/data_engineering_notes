## Web server
Communication between browser and socket server

## socker server job
1. receive information from browser >> wsgiref/gunicorn/uWsgi
    using WSGI protocol to commuting
2. route to different url path depend on demands
3. return specific html file format >> jinja2



## web framework in python 
1. all functions >> Tornado
2. route and return html file >> Django (user wsgiref to satisfy socket commuting)
3. only routing function >> Flask
