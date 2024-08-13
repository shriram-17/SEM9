from flask import Flask,render_template,request


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/submit",methods=['POST'])
def submit_order():
    order = request.form['order']
    return {"order":order}

