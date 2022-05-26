from distutils.log import debug
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', x=8, y=4)

@app.route('/<int:x>')
def rows(x):
    return render_template('index.html', x=x, y=4)

@app.route('/<int:x>/<int:y>')
def rows_columns(x, y):
    return render_template('index.html', x=x, y=y)

@app.route('/<int:x>/<int:y>/<color1>/<color2>')
def colors(x, y, color1, color2):
    return render_template('index.html', x=x, y=y, color1 = color1, color2 = color2)

if __name__ == '__main__':
    app.run(debug=True)