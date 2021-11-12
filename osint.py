print("OSINT Инструменты:")
print("- Обозначения:")
print("(1) - Пробив в терминале.")
print("(2) - Сторонние сервисы.")
print("- Создатель: @darkscreaze")
print("")
print("[1] Список телеграм ботов. (2)")
print("[2] Поиск WhatsApp по номеру телефона. (1)")
print("[3] Поиск по никнейму. (UserRecon) (1)")
print("[4] Информация по BIN номеру банковской карты. (1)")
import os
menu = input("Введите пункт меню > ")
if menu == "1":
    os.system("clear")
    print("- Телеграм боты для пробива:")
    print("")
    print("[Пробив номера телефона] > https://t.me/deanonym_bot")
    print("[GETCONTACT Пробив] > https://t.me/get_kontakt_bot")
    print("[EyeGodsBot] > https://t.me/EyeGodsBot")
    print("[AVInfoBOT] > https://t.me/AVinfoBot")
    print("")
    exit = input("Нажмите ENTER для выхода.")
    if exit == "":
        os.system("clear")
        os.system("python osint.py")
        
        
if menu == "2":
    os.system("clear")
    os.system("python wcheck.py")
    
if menu == "3":
    os.system("clear")
    print("[!] Запуск...")
    os.system("bash nf.sh")
    
if menu == "4":
    os.system("clear")
    os.system("python bincheck.py")