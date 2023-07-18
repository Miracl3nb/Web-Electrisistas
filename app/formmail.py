import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def envio_mail():
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

    cuerpo = 'este mail es de prueba'
    correo.attach(MIMEText(cuerpo, 'plain'))

    #sesion serv mail

    SERVER = smtplib.SMTP('smtp.gmail.com', 587)
    SERVER.starttls()
    SERVER.login(REMITENTE, KEY)


    texto = correo.as_string()
    SERVER.sendmail(REMITENTE, DESTINATARIO, texto)
    SERVER.quit()

