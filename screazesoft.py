import os
import random
import time
import sys
import string
import ctypes
from slowprint.slowprint import *
os.system("clear")
slowprint("\033[32mScreaze Soft v0.7# | Screaze ♡ & Sans", 0.1)
slowprint("[1] - WhatsApp Checker (PN)", 0.1)
slowprint("[2] - Установка смс бомбера", 0.1)
slowprint("[3] - Смс бомбер (Требуется установка из 2 пункта)", 0.1)
slowprint("[4] - Техподдержка", 0.1)
slowprint("[5] - Хакинг", 0.1)
slowprint("[6] - Дединсайд ботнет", 0.1)
slowprint("[7] - Ботнет для телеграмма", 0.1)
slowprint("[8] - Дискорд нитро генератор", 0.1)
slowprint("[9] - Termux-API/Other", 0.1)
slowprint("[10] - Дискорд крашер.", 0.1)
slowprint("[X] - Выход", 0.1)
menu = input("\nВведите пункт из меню: ")
if menu == "1":
	os.system('clear')
	print("WhatsApp Checker | Screaze ♡")
	number = input("Введите номер +")
	print("Ссылки WhatsApp:")
	print("https://api.whatsapp.com/send?phone="+number)
	print("https://wa.me/"+number)
	print("")
	exit = input("Введите 0 для перезапуска! ")
	
if menu == "2":
	os.system('clear')
	code = input("Подтвердите установку! (Y/N)")
	if code == "Y":
		print("Подтверждено, установка...")
		os.system("pip install db0mb3r")
	if code == "N":
		print("Установка отменена!")
		os.system("clear")
		os.system("python screazesoft.py")
if menu == "3":
	print("Запуск...")
	time.sleep(2)
	os.system("b0mb3r")
	exit = input("Введите 0 для перезапуска! ")
	
if menu == "4":
	print("Контакты автора:")
	print("VK: zhernovv")
	print("Telegram: t.me/screaze")
	print("DonationAlerts: donationalerts.com/r/screaze")
	print("Контакты помощника")
	print("Telegram : t.me/sudden_changes_sans")
	print("- Программа создана в образовательных целях! Автор не несёт отвественности за ваши действия.")
	exit = input("Введите 0 для перезапуска!  ")
	
	
if exit == "0":
	os.system("clear")
	os.system("python screazesoft.py")

if menu == "5":
    os.system("clear")
    print("\033[31m!!!ВНИМАНИЕ!!!")
    print("\nПосле соглашения, ответственность за все ваши дальнейшие действия будет лежать на вас!!!")
    hack = input("[y/n] ")
    if hack == "y":
        os.system("clear")
        print("[1] - Установка пентест утилит")
        print("[X] Выход")
        hack2 = input("Введите пункт из меню:  ")
        if hack2 == "1":
            os.system("apt install wget")
            os.system("wget https://raw.githubusercontent.com/gushmazuko/metasploit_in_termux/master/metasploit.sh")
            os.system("chmod +x metasploit.sh")
            os.system("./metasploit.sh")
            os.system("pip install sqlmap")
        
    if hack == "n":
        os.system("clear")
        os.system("python screazesoft.py")
    else:
        os.system("clear")
        os.system("python screazesoft.py")
    if hack2 == "X":
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
 
	
if menu == "9":
	os.system("clear")
	print("[A] - Включить фонарик")
	print("[B] - Выключить фонарик")
	print("[C] - Включить Wi-Fi")
	print("[D] - Выключить Wi-Fi")
	print("[E] - Поставить флаг Украины на обои.")
	print("[N/H] Искатель по нику & Определитель хэшей by sans")
	print("[X] - Назад")
	
menu2 = input("Введите пункт из меню: ")
	
if menu2 == "A":
	os.system("clear")
	print("Фонарик включён.")
	os.system("termux-torch on")
	os.system("python screazesoft.py")

if menu2 == "B":
	os.system("clear")
	print("Фонарик выключен.")
	os.system("termux-torch off")
	os.system("python screazesoft.py")
	
if menu2 == "C":
	os.system("clear")
	print("Wi-Fi Включён!")
	os.system("termux-wifi-enable on")
	os.system("python screazesoft.py")
	
if menu2 == "D":
	os.system("clear")
	print("Wi-Fi Отключён!")
	os.system("termux-wifi-enable off")
	os.system("python screazesoft.py")
	
if menu2 == "E":
	os.system("clear")
	print("Обои устанавливаются...")
	os.system("termux-wallpaper -u https://i.pinimg.com/736x/5d/03/48/5d034835ae769491ae25b4745069cdd9.jpg")
	print("Обои успешно установлены!")
if menu2 == "X":
    os.system("clear")
    os.system("python screazesoft.py")

if menu2 == "Easter Egg":
    os.system("clear")
    print("[1] - Украинцы")
    print("[2] - Немцы")
    egg = input("Выберите пункт из меню:  ")
    if egg == "1":
        os.system("clear")
        os.system('pkg install mpv -y')
        os.system('apt install termux-api -y')
        print("Заскамили москаля")
        os.system('termux-wallpaper -u https://i.pinimg.com/736x/5d/03/48/5d034835ae769491ae25b4745069cdd9.jpg')
        os.system('termux-toast "Слава Украине!"')
        os.system('mpv 1462a1b7ae0a.mp3')
        
        
        	
    if egg == "2":
        os.system("clear")
        os.system('pkg install mpv -y')
        os.system('apt install termux-api -y')
        print("Теперь ты нiмецкiй воiн")
        os.system('termux-wallpaper -u https://images.app.goo.gl/AAnDtBTcRJpVbrSh9')
        os.system('termux-toast "Sieg Heil!"')
        os.system('mpv msi.mp3')
        
    else:
        os.system("clear")
        os.system("python screazesoft.py")
	
if menu2 == "N":
	os.system("clear")
	print("Искатель по нику | Screaze♡")
	print("Сервисов: 17")
	print("Сервисы будут обновляться")
	nickname = input("Введите никнейм: ")
	print("Результаты:")
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

if menu2 == "H":
	os.system("clear")
	os.system("python hashdetector.py")
	
if menu == "10":
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
