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





#funcion de request asiganacion varialble

    """
    def procesar(nombre, correo, texto):
    nombre = request.form[ 'nombre' ]
    correo = request.form[ 'correo' ]
    texto  = request.form[ 'texto' ]
    
    salida = print(f" nombre = {nombre}, correo = {correo}, texto = {texto}")
    
    return salida
    
    
    ///
    
    def envio_mail(nombre:str, correo:str, mensaje:str):
    nombre = request.form['nombre']
    correo = request.form['correo']
    mensaje = request.form['mensaje']
    
    remitente = 'brunel.servicios@gmail.com'
    contraseña = 'P@ss1961!!'
    
    mail_cliente = MIMEMultipart()
    mail_cliente['de'] = remitente
    mail_cliente['para'] = remitente
    mail_cliente['nombre'] = nombre
    
    #cuerpo_correo =
    # Nueva solicitud de contacto!
    #correo: {correo},  mensaje:{mensaje}
    mail_cliente.attach(MIMEText(cuerpo_correo, 'plain'))
    
    servidor_smtp = 'smtp.gmail.com'
    puerto_smtp = 587
    servidor = smtplib.SMTP(servidor_smtp, puerto_smtp)
    servidor.starttls()
    servidor.login(remitente, contraseña)
    servidor.send_message(cuerpo_correo)
    servidor.quit()
    
    pass
    
    
    
    
    """