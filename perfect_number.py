#!/usr/bin/env python
from flask import Flask, request, redirect, url_for, render_template
import math
# create app
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        # show html form
        return render_template('form.html')
    elif request.method == 'POST':
        # calculate result
        a = request.form.get('submit1')
        if a is None:
            a = request.form.get('submit2')

        if a == 'List Numbers':
            start = request.form.get('start')
            end = request.form.get('end')
            return redirect(url_for('list', start=start, end=end))

        if a == 'Is a Perfect Number':
            num = request.form.get('isPerfectNumber')
            return redirect(url_for('perfect', num=num))

@app.route('/list')
def list():
    dict = request.args.to_dict()
    start = int(eval(dict['start']))
    end = int(eval(dict['end']))
    result = []
    while start <= end:

        sum = 0
        divisor = 1
        while divisor < start:
            if not start % divisor:
                sum += divisor
            divisor = divisor + 1
        if sum == start:
            result.append(start)
        start = start + 1

    return 'These are the numbers %s' %result
@app.route('/perfect')
def perfect():
    dict = request.args.to_dict()
    num = eval(dict['num'])
    a = [2, 3, 5, 7, 13, 17, 19, 31, 61, 89, 107, 127, 521, 607, 1279, 2203, 2281, 3217, 4253, 4423, 9689, 9941, 11213,
         19937, 21701, 23209]
    pn = num
    y = 0
    lenght = len(a)
    for i in range(0,lenght):
        s = (math.pow(2, a[i]-1))*(math.pow(2,a[i])-1)
        if s > pn:
            break
        if s == pn:
            y = 1
            return '%s is a perfect number' %num
        if y == 0:
            return '%s is not a perfect number' %num
    return '%s is not a perfect number' %num

# run app
if __name__ == '__main__':
    app.run(debug=True)
