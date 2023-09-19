from flask import Flask, request, render_template
from datetime import datetime
import pandas

import subprocess
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', conteudo=datetime.now().strftime("%H:%M:%S"))

if __name__ == '__main__':
    app.run(host ='0.0.0.0', port = 80, debug = True)
