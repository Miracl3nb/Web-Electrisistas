import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def envio_mail(nombre, email, nota):
    #remitente
    REMITENTE = 'contacto.miracl3dev@gmail.com'
    KEY ='lscuaezfrvcieoqv'
    #destinatario
    DESTINATARIO = 'miracl3nb@gmail.com'
    ASUNTO = 'Nueva solitidud de contacto'

    #mesaje

    correo = MIMEMultipart()
    correo['From'] = REMITENTE
    correo['To'] = DESTINATARIO
    correo['Subjet'] = ASUNTO

    #cuerpo del mensaje

    cuerpo = (f" Nuevo intento de contacto: \n nombre, {nombre} correo {email}  \n nota {nota} ")
    correo.attach(MIMEText(cuerpo, 'plain'))

    #sesion serv mail

    SERVER = smtplib.SMTP('smtp.gmail.com', 587)
    SERVER.starttls()
    SERVER.login(REMITENTE, KEY)


    texto = correo.as_string()
    SERVER.sendmail(REMITENTE, DESTINATARIO, texto)
    SERVER.quit()

