import re

regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

def is_valid_email(email):
# Простая проверка на корректность email
    return re.match(regex, email) is not None

def send_email(message, recipient, sender="unuversity.help@gmail.com"):
# Проверка корретности e-mail отправителя и получателя
    if not is_valid_email(sender):
        return "Некорректный адрес отправителя. Проверьте e-mail."

    if not is_valid_email(recipient):
        return "Некорректный адрес получателя. Проверьте e-mail."

# Проверка на отправку самому себе
    if sender == recipient:
        return "Невозможно отправить письмо самому себе."

def send_email (message,recipient,sender='unuversity.help@gmail.com'):
    if "@" not in recipient or not (recipient.endswith('.com') or recipient.endswith('.ru') or recipient.endswith('.net')):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}.")
    else:
        print(f"Отправляем письмо от {sender})на адрес {recipient} с сообщением: {message}")
    if sender == unuversity.help@gmail.com:
        print (f"Пиьсмо успешно отправлено с адреса {sender} на адрес {recipient}")
    else:
        print (f" НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}")

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
#send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
#send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
#send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')

