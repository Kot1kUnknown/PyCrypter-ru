





#Импорты
from re import findall

# Сердечко криптера
print('''
█▄▀ █▀█ ▀█▀ ▄█ █▄▀   █░█ █▄░█ █▄▀ █▄░█ █▀█ █░█░█ █▄░█
█░█ █▄█ ░█░ ░█ █░█   █▄█ █░▀█ █░█ █░▀█ █▄█ ▀▄▀▄▀ █░▀█
===========================
vk: https://vk.com/kot1kunknown
github: https://github.com/Kot1kUnknown
===========================
	''')

keysen = {
	'А':"142", 'И':"015", 'С':"152",
	'Б':"173", 'Й':"491", 'Т':"164",
	'В':"194", 'К':"130", 'У':"461",
	'Г':"123", 'Л':"486", 'Ф':"787",
	'Д':"432", 'М':"656", 'Х':"676",
	'Е':"321", 'Н':"079", 'Ц':"232",
	'Ё':"146", 'О':"051", 'Ч':"121",
	'Ж':"641", 'П':"150", 'Э':"187",
	'З':"241", 'Р':"060", 'Ю':"781",
	'Я':"163", ' ':"178", '.':"019",
	'?':"198", '!':"901", '(':"910",
	')':"894", ':':"109", ';':"111",
}

cryptmode = input("[E]ncrypt|[D]ecrypt: ").upper()

if cryptmode not in ['E','D']:
	print("Error: вариант выбран не правильно!"); raise SystemExit

startMessage = input("Напиши своё сообщение: ").upper()

def regular(text):
	template = r"\w{3}"
	return findall(template, text)

def encryptDecrypt(mode, message, final = ""):
	if mode == 'E':
		for symbol in message:
			if symbol in keysen:
				final += keysen[symbol]
	else:
		for threeSymbols in regular(message):
			for key in keysen:
				if threeSymbols == keysen[key]:
					final += key

	return final
print("Твоё сообщение:", encryptDecrypt(cryptmode, startMessage))