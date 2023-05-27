from flask import Flask, render_template, request, url_for

app = Flask(__name__)


@app.route("/")
def index():
    context = {
        'title': 'Калькулятор'
    }
    return render_template('index.html', context=context)


@app.route("/result", methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        name = request.form['name']
        birthday = request.form['birthday']
        context = {
            'title': 'Матрица личностей',
            'name': name,
            'birthday': birthday
        }
        print(name)

        print(birthday)
    else:
        context = {
            'title': 'Матрица личностей'
        }
    return render_template('result.html', context=context)


if __name__ == '__main__':
    app.run(debug=True)
