import os
import random
import time
import sys
import string
import ctypes
from slowprint.slowprint import *
# Импорты, можно было в строчку ну ок...
# Бля скриз если ты это читаешь не забудь requirments.txt сделать аутист ебаный
# Уже доделал, сам аутист
crasher = "" # Костыль, не обращайте внимание.
neofetch = "" # Костыль ебать
logo1 = " __                             _     "
logo2 = "(_   _ ._ _   _. _   _   _  _ _|_ _|_ "
logo3 = "__) (_ | (/_ (_| /_ (/_ _> (_) |   |_ [0.9] "
os.system("clear")
print(logo1)
print(logo2)
print(logo3)
print("")
slowprint("[1] - Поиск ватсап по номеру телефона.", 0.1)
slowprint("[2] - Смс бомбер ", 0.1)
slowprint("[4] - Контакты автора", 0.1)
slowprint("[5] - Neofetch (Termux)", 0.2)
slowprint("[6] - Ботнет teleghoul", 0.1)
slowprint("[7] - Ботнет для телеграмма.", 0.1)
slowprint("[8] - Дискорд нитро генератор с вебхуком и чекингом.", 0.1)
slowprint("[9] - Бросить кубик (Забавы ради)", 0.1)
slowprint("[10] - Дискорд краш бот.", 0.1)
slowprint("[11] - DDoS Атака по url (HTTP Flood)", 0.1)
slowprint("[12] - Определение типа хэша.", 0.1)
slowprint("[13] - Пробив по никнейму (слабый)", 0.1)
slowprint("[14] - Генератор деанонов", 0.2)
slowprint("[15] - Бомбер электронной почты", 0.3)
slowprint("[16] - Блокировка ВКонтакте по токену.", 0.1)
slowprint("[X] - Выход", 0.1)
menu = input("Введите пункт из меню > ")
if menu == "1":
	os.system('clear')
	print("WhatsApp Checker | Screaze ♡")
	number = input("Введите номер +")
	print("Ссылки WhatsApp:")
	print("https://api.whatsapp.com/send?phone="+number)
	print("https://wa.me/"+number)
	print("")
	exit = input("Введите 0 для перезапуска! ")

# b0mb3r меню

if menu == "2":
    os.system("clear")
    print("B0MB3R MENU")
    print("")
    print("[1] Запуск")
    print("[2] Установка")
    print("[3] Информация")
    
    bomber = input("Введите пункт меню > ") 
    
    if bomber == "1":
        os.system("clear")
        print("Откройте новую сессию и запустите screazesoft.py вручную для дальнейшего использования с бомбером!")
        os.system("b0mb3r") # Запуск
        
    if bomber == "3":
           os.system("clear")
           print("Информация:")
           print("=============")
           print("Сервисы: 124")
           print("Dev: crinny")
           print("=============")
           print("")
           exit = input("Введите 0 для выхода > ")
           # Инфо
           
    if bomber == "2":
        os.system("clear")
        bomber1 = input("Подтвердите установку (Y/N) > ")
        if bomber1 == "Y":
            os.system("clear")
            print("УстановОчка...")
            os.system("pip install db0mb3r")
            os.system("clear")
            os.system("python screazesoft.py")
        if bomber1 == "N":
            print("Отмена!")
            os.system("clear")
            os.system("python screazesoft.py")
            # Установщик
            
            


if menu == "4":
	print("Контакты автора:")
	print("VK: lipeckiyscreaze")
	print("Telegram: t.me/screaze")
	print("DonationAlerts: https://donationalerts.com/r/screaze")
	print("- Программа создана в образовательных целях! Автор не несёт отвественности за ваши действия.")
	exit = input("Введите 0 для перезапуска!  ")
	
	
if exit == "0":
	os.system("clear")
	os.system("python screazesoft.py")
        
if menu == "6":
    os.system("clear")
    answ = str(input("Хотите ли вы открыть конфиг для настройки ботнета? [y/n/x]  "))
    if answ == "y":
        os.system("nano configghoul.py ")
    if answ == "n":
        os.system("python ghoul.py")
    if answ == "x":
        os.system("clear")
        os.system("python screazesoft.py")

    
    
	
if menu == "7":
    os.system("clear")
    answ2 = str(input("Хотите ли вы открыть конфиг для настройки ботнета? [y/n/x]  "))
    if answ2 == "y":
        os.system("nano config.ini")
    if answ2 == "n":
        os.system("python botnet.py")
    if answ2 == "x":
        os.system("clear")
        os.system("python screazesoft.py")
    else:
        print("Неизвестный параметр!")
        time.sleep(2)
        os.system("clear")
        os.system("python screazesoft.py")

if menu == "X":
    print("Выход...")
    sys.exit()

if menu == "8":
    os.system("clear")
    os.system("python checker.py")
 
	
	
if menu == "13":
	os.system("clear")
	print("Искатель по нику | Screaze♡")
	print('Сервисов: 15')
	nickname = input("Введите никнейм: ")
	print("Результаты:")
	print("")
	print("t.me/"+nickname)
	print("donationalerts.com/r/"+nickname)
	print("https://vk.com/"+nickname)
	print("https://github.com/"+nickname)
	print("https://instagram.com/"+nickname)
	print("https://facebook.com/"+nickname)   
	print("https://"+nickname+".wordpress.com")
	print("https://pinterest.com/"+nickname)
	print("https://twitter.com/"+nickname)
	print("https://youtube.com/"+nickname)
	print("https://reddit.com/user/"+nickname)
	print("https://"+nickname+".tumblr.com")
	print("https://www.flickr.com/people/"+nickname)
	print("https://vimeo.com/"+nickname)
	print("https://soundcloud.com/"+nickname)
	exit = input("Введите 0 для выхода: ")
	
	if exit == "0":
		os.system("clear")
		os.system("python screazesoft.py")

if menu == "12":
	os.system("clear")
	os.system("python hashdetector.py")
	

if menu == "11":
    os.system("clear")
    os.system("python ddos.py")
    os.system("python screazesoft.py")

if menu == "10":
	crasher == ""
	os.system("clear")
	print("Дискорд крашер:")
	print("[1] - Открыть конфиг")
	print("[2] - Открыть список команд")
	print("[3] - Запустить бота.")
	print("[X] - Выйти.")
	crasher = input("Введите пункт меню > ")


if crasher == "X":
	os.system("clear")
	os.system("python screazesoft.py")
	
if crasher == "1":
	os.system("clear")
	os.system("nano raidcfg.ini")
	os.system("python screazesoft.py")

if crasher == "2":
  	os.system("nano cmd.txt")
  	os.system("python screazesoft.py")
  	
if crasher == "3":
	os.system("clear")
	os.system("python modded.py")

if menu == "9":
    os.system('clear')
    slowprint("Кубик падает...", 0.3)
    sleep(2)
    print("Ваше число:")
    number5 = random.randint(1, 6)
    print(number5)
    print('')
    exit = input("Введите 0 для выхода > ")
    if exit == "0":
        os.system("python screazesoft.py")
        
if menu == "5":
   os.system("clear")
   neofetch = input("Установить/Установлен Neofetch? (I/Y/N) > ")
   if neofetch == "Y":
       os.system("clear")
       os.system("neofetch")
       exit = input("Введите 0 для выхода!  ")
       if exit == "0":
           os.system("clear")
           os.system("python screazesoft.py")
   if neofetch == "I":
       os.system("clear")
       os.system("pkg install neofetch")
       
   if neofetch == "N":
       os.system("clear")
       print("Установи...")
       os.system("python screazesoft.py")
        
if menu == "14":
    os.system("clear")
    os.system("python deanongen.py")

if menu == "15":
    os.system("clear")
    os.system("python mailbomb.py")

if menu == "16":
    os.system("clear")
    os.system("python fastban.py")


