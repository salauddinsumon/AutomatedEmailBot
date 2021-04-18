import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
#need to gmail and change security credential
server.login('user.email adress','Password')
server.sendmail('receiver email',' mail body-hi sam you are now on your track')