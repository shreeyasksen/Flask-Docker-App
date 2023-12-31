from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_geek():
    return '<h1>Hello My name is shreeyasen i am doing Flask & Docker</h2>'


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=4000)