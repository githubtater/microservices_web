#!/usr/bin/env python3

import time
from flask import Flask, render_template
import os

app = Flask(__name__)

try:
    os.environ['SECRET_KEY'] = open('key').read().strip()
    app.secret_key = os.environ.get('SECRET_KEY').encode()
except AttributeError:
    print('Environment variable not found: SECRET_KEY')


@app.route('/')
def home():
    current_time = time.time()
    return render_template('base.jinja2', current_time=current_time)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6738))
    app.run(host='localhost', port=port)