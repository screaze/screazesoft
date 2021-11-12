import os
os.system('clear')
print("- Поиск WhatsApp по номеру телефона.")
print("- Dev: @darkscreaze")
print("")
number = input("Введите номер +")
print("Ссылки WhatsApp:")
print("https://api.whatsapp.com/send?phone="+number)
print("https://wa.me/"+number)
print("")
exit = input("Введите ENTER для выхода")
if exit == "":
    os.system("clear")
    os.system("python osint.py")
