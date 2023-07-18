from flask import Flask, render_template
from formmail import envio_mail

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contacto', method=['POST'])
def contacto():
    pass

if __name__ == '__main__':
    app.run(debug=True, port=5000)



#funcion de request asiganacion varialble

    """
    def procesar(nombre, correo, texto):
    nombre = request.form[ 'nombre' ]
    correo = request.form[ 'correo' ]
    texto  = request.form[ 'texto' ]
    
    salida = print(f" nombre = {nombre}, correo = {correo}, texto = {texto}")
    
    return salida
    
    
    
    
    
    
    
    """