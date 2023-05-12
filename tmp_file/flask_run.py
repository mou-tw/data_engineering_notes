from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/',methods=['POST','GET'])
def test():
    print(request)
    if request.method == "POST":
        return render_template('chat.html')
    
    return render_template('chat.html')

if __name__ == "__main__":
    app.run(debug=True)