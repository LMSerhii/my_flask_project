import os
from datetime import datetime

from flask import Flask, render_template, request, url_for, flash
from dotenv import load_dotenv

load_dotenv()
SECRET_KEY = os.getenv('SECRET_KEY')

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY


@app.route("/")
def index():
    context = {
        'title': 'Калькулятор'
    }
    return render_template('index.html', context=context)


@app.route("/result", methods=['POST', 'GET'])
def result():
    def num_sum(num):
        num = int(num)
        if num > 27:
            return num_sum(sum(map(int, list(str(num)))))
        return num

    if request.method == 'POST':
        day = request.form['day']
        month = request.form['month']
        year = request.form['year']

        birthday = f'{day}.{month}.{year}'

        name = request.form['name']

        if not day.isdigit():
            flash("Поле День должно содержать только цифры")
        else:
            if int(day) > 31:
                flash("Дней не может быть больше 31")
                context = {
                    'title': 'Матрица личностей',
                }
                return render_template('index.html', context=context)

        if not month.isdigit():
            flash("Поле Месяц должно содержать только цифры")
        else:
            if int(month) > 12:
                flash("Месяцев не может быть больше 12")
                context = {
                    'title': 'Матрица личностей',
                }
                return render_template('index.html', context=context)

        if not year.isdigit():
            flash("Поле Год должно содержать только цифры")
        else:
            if 1900 > int(year) or int(year) > datetime.now().year:
                flash(f"Год должен быть в диапазоне от 1900 до {datetime.now().year}")
                context = {
                    'title': 'Матрица личностей',
                }
                return render_template('index.html', context=context)

        if day.isdigit() and month.isdigit() and year.isdigit():
            month = num_sum(month)  # первый сверху
            day = num_sum(day)  # первый слева
            year = num_sum(year)  # первый справа

            f_1 = num_sum((day + month + year))  # Первый снизу
            f_2 = num_sum((f_1 + day + month + year))  # центр

            f_3 = num_sum((day + f_2))  # третий слева
            f_4 = num_sum((day + f_3))  # второй слева

            f_5 = num_sum((month + f_2))  # третий сверху
            f_6 = num_sum((month + f_5))  # второй сверху

            f_7 = num_sum((year + f_2))  # третий справа
            f_8 = num_sum((year + f_7))  # второй справа

            f_9 = num_sum((f_1 + f_2))  # третий снизу
            f_10 = num_sum((f_1 + f_9))  # второй снизу

            f_11 = num_sum((f_7 + f_9))  # четвертый правый-низ
            f_12 = num_sum((f_11 + f_9))  # love
            f_13 = num_sum((f_7 + f_11))  # money

            f_14 = num_sum((day + f_1))  # первый левый-низ
            f_18 = num_sum((f_2 + f_14))  # третий левый-низ
            f_19 = num_sum((f_18 + f_14))  # второй левый-низ

            f_15 = num_sum((year + f_1))  # первый правый-низ
            f_20 = num_sum((f_2 + f_15))  # третий правый-низ
            f_21 = num_sum((f_20 + f_15))  # второй правый-низ

            f_16 = num_sum((year + month))  # первый правый-верх
            f_22 = num_sum((f_2 + f_16))  # третий правый-верх
            f_23 = num_sum((f_22 + f_16))  # второй правый-верх

            f_17 = num_sum((day + month))  # первый левый-верх
            f_24 = num_sum((f_2 + f_17))  # третий левый-верх
            f_25 = num_sum((f_24 + f_17))  # второй левый-верх

            #####################################################

            s_1 = num_sum((f_24 + f_22 + f_20 + f_18))  # 4 низ
            s_2 = num_sum((f_25 + f_23 + f_21 + f_19))  # 3 низ
            s_3 = num_sum((f_17 + f_16 + f_15 + f_14))  # 2 низ
            s_4 = num_sum((f_24 + f_20))  # правый низ от центра
            s_5 = num_sum((f_22 + f_18))  # левый низ от центра

            context = {
                'title': 'Матрица личностей',
                'birthday': birthday,
                'name': name,
                'year': year,
                'day': day,
                'month': month,
                'f_1': f_1,
                'f_2': f_2,
                'f_3': f_3,
                'f_4': f_4,
                'f_5': f_5,
                'f_6': f_6,
                'f_7': f_7,
                'f_8': f_8,
                'f_9': f_9,
                'f_10': f_10,
                'f_11': f_11,
                'f_12': f_12,
                'f_13': f_13,
                'f_14': f_14,
                'f_15': f_15,
                'f_16': f_16,
                'f_17': f_17,
                'f_18': f_18,
                'f_19': f_19,
                'f_20': f_20,
                'f_21': f_21,
                'f_22': f_22,
                'f_23': f_23,
                'f_24': f_24,
                'f_25': f_25,
                's_1': s_1,
                's_2': s_2,
                's_3': s_3,
                's_4': s_4,
                's_5': s_5,
            }
            return render_template('result.html', context=context)

    context = {
        'title': 'Матрица личностей',
    }
    return render_template('index.html', context=context)


if __name__ == '__main__':
    app.run()
