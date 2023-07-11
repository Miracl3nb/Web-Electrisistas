"""
    from flask import Flask, request, render_template
import smtplib

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def contact_form():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        
        # Configura los detalles de tu servidor SMTP
        smtp_server = 'tu_servidor_smtp'
        smtp_port = 587
        smtp_username = 'tu_usuario_smtp'
        smtp_password = 'tu_contraseña_smtp'
        sender_email = 'tu_email_de_origen'
        receiver_email = 'tu_email_de_destino'
        
        # Crea el cuerpo del correo electrónico
        subject = 'Nuevo mensaje de contacto'
        body = f'Nombre: {name}\nEmail: {email}\nMensaje: {message}'
        message = f'Subject: {subject}\n\n{body}'
        
        # Envía el correo electrónico
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.sendmail(sender_email, receiver_email, message)
        
        return 'Mensaje enviado correctamente'
    
    return render_template('contact_form.html')

if __name__ == '__main__':
    app.run()
    
    
    
    """