import os
import random
import time
os.system("clear")
print("Screaze Soft v0.5#BETA |  Screaze ♡")
print("[1] WhatsApp Checker (PN)")
print("[2] Установка смс бомбера")
print("[3] Смс бомбер (Требуется установка из 2 пункта)")
print("[4] Техподдержка")
print("[5] Termux-API/Other")
print("[6] Телеграм ботнет (баганный)")
print("\nПосле того как вы сделали в нужном вам пункте перезапустите .py, если он не предложил вам это сделать/не сделал автоматически!")
print("\nХэш детектор и ботнет сейчас забагованны.")
menu = input("\nВведите пункт меню: ")
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
	print("[A] Включить фонарик")
	print("[B] Выключить фонарик")
	print("[C] Включить Wi-Fi")
	print("[D] Выключить Wi-Fi")
	print("[E] Поставить флаг Украины на обои.")
	print("[F/G] NickName Finder / Hash Detector by sans")
menu2 = input("Введите пункт меню: ")
if menu == "6":
    os.system("clear")
    os.system("pip install -r requirements.txt")
    
    
	
	
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

if menu2 == "Easter Egg":
        os.system("clear")
        print("You found Easter Egg!")
        ukraina = input("У вас есть Termux:API? (Y/N)")
        if ukraina == "Y":
        	os.system("clear")
        	os.system("python ukraina.py")
        	
        if ukraina == "N":
        	os.system("clear")
        	os.system("python screazesoft.py")
	
if menu2 == "F":
	os.system("clear")
	print("NickName Finder | Screaze♡")
	print("Сервисов: 4")
	print("Сервисы будут обновляться")
	nickname = input("Введите никнейм: ")
	print("Результаты:")
	print("t.me/"+nickname)
	print("donationalerts.com/r/"+nickname)
	print("https://vk.com/"+nickname)
	print("https://github.com/"+nickname)
	print("В будущем добавлю ещё.")
	exit = input("Введите 0 для выхода: ")
	
	if exit == "0":
		os.system("clear")
		os.system("python screazesoft.py")

if menu2 == "G":
	os.system("clear")
	os.system("python hashdetect.py")
else:
    print("Неизвестное действие!")
    time.sleep(2)
    os.system("clear")
    os.system("python screazesoft.py")
menu3 = input("Хотите ли вы открыть конфиг для настройки вашего Api Id И Api Hash? [y/n]  ")
if menu3 == "n":
    os.system("python botnet.py")
if menu3 == "y":
    os.system("nano config.ini")