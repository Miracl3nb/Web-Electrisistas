from flask import Flask, render_template, request
from formmail import envio_mail

app = Flask(__name__)




@app.route('/')
def index():
    return render_template('index.html')


@app.route('/solicitud_contacto/',  methods = ['POST', 'GET'] )
def contacto():
    nombre = request.form['name']
    correo = request.form[ 'correo' ]
    texto  = request.form[ 'mensaje' ]
    
    envio_mail(nombre, correo, texto)
    return index() 


if __name__ == '__main__':
    app.run(debug=True, port=5000)
