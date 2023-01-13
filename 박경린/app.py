from flask import Flask,render_template, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World"

@app.route('/sql')
def index():
    return render_template('index.html')

@app.route('/command', methods=['POST'])
def command():
    
    return "TEST"+ request.form.get('first_test') # render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)