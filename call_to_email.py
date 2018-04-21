import smtplib
from moex_bot.list_to_email import list_to

login = 'moexregina@gmail.com'
password = 'regina2018'
address_to = 'mkryukov1970@gmail.com'  # адрес куда отправить письмо
address_from = 'moexregina@gmail.com'  # адрес от куда отправлено письмо
to = 'Maxim'  # имя для кого письмо


# функлия отпровляет рекомендации на e-mail
def email():
    signal = list_to()
    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.login(login, password)
    message = '\r\n'.join([
        'From: Stock_bot',
        'To: {}'.format(to),
        'Subject: Signal',
        '', '\n'.join(signal)]).encode('utf-8')
    smtpObj.sendmail(address_from, address_to, message)
    smtpObj.quit()


if __name__ == "__main__":
    email()
