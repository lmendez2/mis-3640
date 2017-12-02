"""
Simple "Hello, World" application using Flask
"""
from flask import Flask, render_template, request, redirect, url_for
import math
from mbta_helper import find_stop_near

app = Flask(__name__)

app.config['DEBUG'] = True


@app.route('/',methods=['GET','POST'])
def find_stop():
    if request.method == 'POST':
        place = request.form['userloc']
        stop, distance = find_stop_near(place)
        print(stop)
        print(distance)
        return render_template('results.html', stop = stop, distance=distance)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host ='127.0.0.1', port=5000)