import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from decouple import config

def envio_mail(nombre, email, nota):
    #remitente
    REMITENTE = config('REMITENTE')
    KEY = config('KEY')
    #destinatario
    DESTINATARIO = config('DESTINATARIO')
    
    ASUNTO = 'Nueva solitidud de contacto'

    #mesaje

    correo = MIMEMultipart()
    correo['From'] = REMITENTE
    correo['To'] = DESTINATARIO
    correo['Subjet'] = ASUNTO

    #cuerpo del mensaje

    cuerpo = (f" Nuevo intento de contacto: \n Nombre: {nombre}\n Correo: {email}  \n Nota: {nota} ")
    correo.attach(MIMEText(cuerpo, 'plain'))

    #sesion serv mail

    SERVER = smtplib.SMTP('smtp.gmail.com', 587)
    SERVER.starttls()
    SERVER.login(REMITENTE, KEY)


    texto = correo.as_string()
    SERVER.sendmail(REMITENTE, DESTINATARIO, texto)
    SERVER.quit()

