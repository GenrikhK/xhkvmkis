from flask import Flask, render_template

app = Flask(__name__)






@app.route('/')
def index():
    return render_template('index.html')

@app.route('/info')
def info():
    return 'there will be some info...'

if __name__ == '__main__':
    app.run(host='0.0.0.0')

