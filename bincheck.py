# Developer: t.me/darkscreaze
print("[?] Dev: @darkscreaze")
print("[?] Поиск информации по BIN банковской карты.")
from requests import get
from sys import argv
from prettytable import PrettyTable
ABOBA = "[!] Перезапустите вручную screazesoft.py/osint.py!"
def _check_(cc):
	p =b= None
	T   = PrettyTable()
	r 	= get(f"https://lookup.binlist.net/{cc}",
		headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36', 
		"Accept-Version": "3"}).json()
	try: 
		if r["prepaid"]: p = r["prepaid"]
		if r["bank"]: b = f'{r["bank"]["name"]}({r["bank"]["url"]})'
	except: pass
	T.field_names = ['CARD NUM','CARD SCHEME', 'CARD TYPE', 'CARD BRAND', 'CARD PREPAID', 'CARD COUNTRY', 'CARD BANK']
	T.add_row([cc,r["scheme"], r["type"], r["brand"], p, f'{r["country"]["name"]}({r["country"]["emoji"]} )', b])
	print(T)
	print(ABOBA)

if __name__ == '__main__':
	while 1:
		try:
			if len(argv)==2:
				if len(argv[1]) >= 6: _check_(argv[1]); break
				else:
					cc = input("[?] Введите первые 6 цифр банковской карты > ").replace(" ", "")
					if len(cc) >= 6: _check_(cc); break
			else:
				cc = input("[?] Введите первые 6 цифр банковской карты > ").replace(" ", "")
				if len(cc) >= 6: _check_(cc)
		except KeyboardInterrupt: print("\nПока!"); os.system("python osint.py, clear")
		except EOFError: print("\nПока!"); os.system("python osint.py, clear")
