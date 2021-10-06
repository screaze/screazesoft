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
Telegram BotNet v0.2 ♡
[$] Рабочих аккаунтов >> {accounts}
[$] Удаленных аккаунтов >> {dead}

[0] – Изменить кол-во аккаунтов.
[1] – Зайти в беседу/канал.
[2] – Выйти из беседы/канала.
[3] - Флуд в чат/беседу (text)
[4] – Флуд в чат/беседу (gif)
[5] – Флуд в чат/беседу (voice)
[6] – Флуд в чат/беседу (photo)
[7] – Флуд в чат/беседу (sticker)
[8] – Рестарт
[9] – Выход
""")
        action = input('>> ')
        if action == "0" or action == "1" or action == "2" or action == "3" or action == "4" or action == "5" or action == "6" or action == "7" or action == "8" or action == "9":
            run = 1
        else:
            print('[x] Неизвестная команда!')
            sleep(1)

    if action == '0':
        from editaccounts import sessiones
        print('\033[32m[√] Перезагрузка ботнета')
        os.execl(sys.executable, sys.executable, *sys.argv)
        quit()

    if action == '1':
        group = input('\033[31mUsername>> \033[39m')
        ping = perf()
        for _ in app:
            try:
                app[_].join_chat(group)
                print(f'\033[32m[v] {_} зашёл в @{group}')
            except:
                print(f'\033[31m[x] {_} не может зайти в @{group}')
        print(f'\033[33m[√] Все аккаунты зашли в @{group}')
        input('\033[32m[*] Нажмите ENTER')


    if action == '2':
        group = input('\033[31mUsername>> \033[39m')
        ping = perf()
        for _ in app:
            try:
                app[_].leave_chat(group)
                print(f'\033[32m[v] {_} аккаунт вышел из @{group}')
            except:
                print(f'\033[31m[x] {_} аккаунт не может выйти из @{group}')
        print(f'\033[32m[√] Все аккаунтц вышли из @{group}')
        input('\033[32m[*] Нажмите ENTER.')


    if action == '3':
        group = input('\033[31mUsername>> \033[39m')
        text = input('\033[31mText>> \033[39m')

        msgs = int(input('\033[31m Кол-во сообщений (Для всех аккаунтов)>> \033[39m'))
        cooldown = int(input('\033[31mЗадержка в секундах (советую 3-5) >> \033[39m'))
        sms = 0
        ping = perf()
        for z in range(msgs):
            for _ in app:
                try:
                   app[_].send_message(group, text)
                   sms += 1
                   print(f'\033[32m[v] {_} аккаунт отправил {sms} сообщение в @{group}')
                   sleep(cooldown)
                except:
                   print(f'\033[31m[x] {_} аккаунт не смог отправить сообщение в @{group}')
        print(f'\033[32m[√] Все сообщения отправлены в @{group}')
        input('\033[32m[*] Нажмите ENTER.')


    if action == '4':
        print(f'\033[32mTo continue you must to put gif.gif to folder with BotNet!')
        group = input('\033[31mUsername>> \033[39m')
        gif = "gif.gif"
        text = input('\033[31mText>> \033[39m')

        msgs = int(input('\033[31mMessages count (from every account)>> \033[39m'))
        cooldown = int(input('\033[31mCooldown>> \033[39m'))
        sms = 0
        ping = perf()
        for z in range(msgs):
            sleep(cooldown)
            for _ in app:
                try:

                     app[_].send_animation(group, gif, caption=text)
                     sms += 1
                     print(f'\033[32m[v] {_} account sent {sms} gif to @{group}')
                except:
                        print(f'\033[31m[x] {_} account cannot send gif to @{group}')
        print(f'\033[32m[√] All gifs sent to @{group}')
        input('\033[32m[*] Press ENTER to continue')


    if action == '5':
        print(f'\033[32mTo continue you must to put sound.mp3 to folder with BotNet!')
        group = input('\033[31mUsername>> \033[39m')
        voice = "sound.mp3"
        text = input('\033[31mText>> \033[39m')

        msgs = int(input('\033[31mVoices count (from every account)>> \033[39m'))
        cooldown = int(input('\033[31mCooldown>> \033[39m'))
        sms = 0
        ping = perf()
        for z in range(msgs):
            sleep(cooldown)
            for _ in app:
                try:

                     app[_].send_voice(group, voice, caption=text)
                     sms += 1
                     print(f'\033[32m[v] {_} account sent {sms} voice to @{group}')
                except:
                        print(f'\033[31m[x] {_} account cannot send voice to @{group}')
        print(f'\033[32m[√] All voices sent to @{group}')
        input('\033[32m[*] Press ENTER to continue')


    if action == '6':
        print(f'\033[32mTo continue you must to put photo.jpg to folder with BotNet!')
        group = input('\033[31mUsername>> \033[39m')
        photo = "photo.jpg"
        text = input('\033[31mText>> \033[39m')

        msgs = int(input('\033[31mPhotos count (from every account)>> \033[39m'))
        cooldown = int(input('\033[31mCooldown>> \033[39m'))
        sms = 0
        ping = perf()
        for z in range(msgs):
            sleep(cooldown)
            for _ in app:
                try:

                     app[_].send_photo(group, photo, caption=text)
                     sms += 1
                     print(f'\033[32m[v] {_} account sent {sms} photo to @{group}')
                except:
                        print(f'\033[31m[x] {_} account cannot send message to @{group}')
        print(f'\033[32m[√] All photos sent to @{group} ')
        input('\033[32m[*] Press ENTER to continue')


    if action == '7':
        group = input('\033[31mUsername>> \033[39m')
        print(f'\033[32mTo get sticker id you must to send sticker to @stickerid2_bot and copy id.')
        sticker = input('\033[31mSticker ID>> \033[39m')
        msgs = int(input('\033[31mStickers count (from every account)>> \033[39m'))
        cooldown = int(input('\033[31mCooldown>> \033[39m'))
        sms = 0
        ping = perf()
        for z in range(msgs):
            sleep(cooldown)
            for _ in app:
                try:

                     app[_].send_sticker(group, sticker)
                     sms += 1
                     print(f'\033[32m[v] {_} account sent {sms} sticker to @{group}')
                except:
                        print(f'\033[31m[x] {_} account cannot send sticker to @{group}')
        print(f'\033[32m[√] All messages sent to @{group} ')
        input('\033[32m[*] Press ENTER to continue')


    if action == '8':
        print('\033[32m[√] Restarting botnet...')
        os.execl(sys.executable, sys.executable, *sys.argv)
        quit()


    if action == '9':
        print("\033[32m[√] Выход...")
        os.system("clear")
        os.system("python screazesoft.py")


idle()
