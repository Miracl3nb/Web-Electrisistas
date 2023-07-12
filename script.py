
from flask import Flask, request, render_template
import smtplib

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def holamundo():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
    
    
