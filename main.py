from flask import Flask

app = Flask(__name__)

@app.route('/')
def hola():
    return "Hola Mundo del Moli"


if __name__ == '__main__':
        app.run(debug=True, port=5021)    

