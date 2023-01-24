import smtplib
from decouple import config 

message = 'Este es el primer mensaje desde Python que se envia '
subject = 'Test de correo'
message = 'Subject: {}\n\n{}'.format(subject, message)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('hcontreras@academicos.uta.cl', config('MAIL_PASSWORD')) #crear un archivo .env donde se almacena la variable MAIL_PASSWORD

server.sendmail('<insertar-correo-remitente>', '<insertar-correo-destinatario',message) 

server.quit()

print("Listo, el correo se ha enviado satisfactoriamente!")