from datetime import datetime as date
from time import sleep
from time import perf_counter as perf
import os, sys, colorama, logging
from pyrogram import Client, filters
from pyrogram.errors import FloodWait, ChatSendMediaForbidden
from pyrogram.types import Message, ChatPermissions
from pyrogram.handlers import MessageHandler
from accounts import sess

logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("pyrogram").setLevel(logging.CRITICAL)
logging.getLogger("sess").setLevel(logging.WARNING)
logging.getLogger("sess").setLevel(logging.ERROR)
logging.getLogger("sess").setLevel(logging.CRITICAL)

os.system('cls' if os.name == 'nt' else 'clear')

app = sess

acc = 0
dead = 0
accounts = 0

for _ in app:
    try:
        app[_].start()
        me = app[_].get_me()
        accounts += 1
        acc += 1
        print(f'\033[32m[{acc}√] {me.first_name} - ({me.id}) started!')

    except Exception as exc:
        dead += 1
        acc += 1
        print(f'\033[31m[{acc}x] Cannot start \n{exc}')

while True:
    run = 666
    while run != 1:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"""
[$] Рабочих аккаунтов > {accounts}
[$] Мёртвых аккаунтов > {dead}

[1] – Зайти в чат
[2] – Выйти из чата
[3] – Спам в чат (text)
[4] – Спам в чат (gif)
[5] – Спам в чат (voice)
[R] – Перезагрузка
[E] - Изменить кол-во аккаунтов
[X] – Выход
""")
        action = input('>> ')
        if action == "0" or action == "1" or action == "2" or action == "3" or action == "4" or action == "5" or action == "6" or action == "7" or action == "8" or action == "9":
            run = 1
        else:
            print('[x] Неизвестная команда!')
            sleep(2)

    if action == 'E':
        from editaccounts import sessiones
        print('\033[32m[√] Перезагрузка ботнета')
        os.execl(sys.executable, sys.executable, *sys.argv)
        quit()

    if action == '1':
        group = input('\033[31mЧат > \033[39m')
        ping = perf()
        for _ in app:
            try:
                app[_].join_chat(group)
                print(f'\033[32m[v] {_} зашёл в @{group}')
            except:
                print(f'\033[31m[x] {_} не зашёл в @{group}')
        print(f'\033[33m[√] Все аккаурты зашли в @{group}')
        input('\033[32m[*] Нажмите enter чтобы продолжить')


    if action == '2':
        group = input('\033[31mЧат > \033[39m')
        ping = perf()
        for _ in app:
            try:
                app[_].leave_chat(group)
                print(f'\033[32m[v] {_} вышел из @{group}')
            except:
                print(f'\033[31m[x] {_} не вышел из @{group}')
        print(f'\033[32m[√] Все аккаунты вышли из @{group}')
        input('\033[32m[*] Нажмите ENTER для продолжения.')


    if action == '3':
        group = input('\033[31mЧат > \033[39m')
        text = input('\033[31mТекст > \033[39m')

        msgs = int(input('\033[31mСообщений > \033[39m'))
        cooldown = int(input('\033[31mКд > \033[39m'))
        sms = 0
        ping = perf()
        for z in range(msgs):
            for _ in app:
                try:
                   app[_].send_message(group, text)
                   sms += 1
                   print(f'\033[32m[v] {_} отправил {sms} в @{group}')
                   sleep(cooldown)
                except:
                   print(f'\033[31m[x] {_} не смог отправить сообщение в @{group}')
        print(f'\033[32m[√] Все сообщения отправлены в  @{group}')
        input('\033[32m[*] Нажмите ENTER чтобы продолжить')


    if action == '4':
        print(f'\033[32mЧтобы продолжить добавьте в директорию gif.gif')
        group = input('\033[31mЧат > \033[39m')
        gif = "gif.gif"
        text = input('\033[31mТекст > \033[39m')

        msgs = int(input('\033[31mКол-во сообщений > \033[39m'))
        cooldown = int(input('\033[31mКД > \033[39m'))
        sms = 0
        ping = perf()
        for z in range(msgs):
            sleep(cooldown)
            for _ in app:
                try:

                     app[_].send_animation(group, gif, caption=text)
                     sms += 1
                     print(f'\033[32m[v] {_} отправил {sms} и gif в @{group}')
                except:
                        print(f'\033[31m[x] {_} не смош отправить gif в @{group}')
        print(f'\033[32m[√] Все gif отправлены в  @{group}')
        input('\033[32m[*] Нажмите enter чтобы продолжить.')


    if action == '5':
        print(f'\033[32mЧтобы продолжить добавьте в директорию файл sound.mp3')
        group = input('\033[31mЧат > \033[39m')
        voice = "sound.mp3"
        text = input('\033[31mТекст > \033[39m')

        msgs = int(input('\033[31mКол-во сообщений > \033[39m'))
        cooldown = int(input('\033[31mКД > \033[39m'))
        sms = 0
        ping = perf()
        for z in range(msgs):
            sleep(cooldown)
            for _ in app:
                try:

                     app[_].send_voice(group, voice, caption=text)
                     sms += 1
                     print(f'\033[32m[v] {_} отправил {sms}голосове в @{group}')
                except:
                        print(f'\033[31m[x] {_} не смог отправить в  @{group}')
        print(f'\033[32m[√] Все войсы отправлены в @{group}')
        input('\033[32m[*] Нажмите ENTER чтобы продолжить.')






    if action == 'R':
        print('\033[32m[√] Перезагрузка ботнета...')
        os.execl(sys.executable, sys.executable, *sys.argv)
        quit()


    if action == 'X':
        print("\033[32m[√] Выход...")
        os.system("clear")
        os.system("python screazesoft.py")


idle()
