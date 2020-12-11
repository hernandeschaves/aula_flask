from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello world</h1>"

@app.route('/alo')
@app.route('/mamae')
def alo():
    return "<h1>Alô mamãe</h1>"

if __name__ == '__main__':
    app.run()