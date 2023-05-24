from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    context = {
        'title': 'Калькулятор'
    }
    return render_template('index.html', context=context)


@app.route("/result")
def result():
    return render_template('result.html')


if __name__ == '__main__':
    app.run(debug=True)
