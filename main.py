import json

class Noun:
	is_animacy = False	# Одушевлённое
	is_nomen = False	# Собственное
	gender = 1			# Род
	number = False		# Число
	case = 1			# Падеж
	
	def toDict(self):
		return {
		"type" : "Noun",
		"is_animacy" : self.is_animacy,
		"is_nomen" : self.is_nomen,
		"gender" : self.gender,
		"number" : self.number,
		"case" : self.case,
		}
		
class Verb:
	gender = 1			# Род
	number = False		# Число
	time = 1			# Время
	
	def toDict(self):
		return {
		"type" : "Verb",
		"gender" : self.gender,
		"number" : self.number,
		"time" : self.time,
		}

def createNoun():
	obj = Noun()
	
	obj.is_animacy = input("Одушевлённое? (y/n): ") == "y"
	obj.is_nomen = input("Имя собственное? (y/n): ") == "y"
	obj.number = input("Число множественное? (y/n): ") == "y"
	
	print("Род")
	print("1.Мужской")
	print("2.Женскицй")
	print("3.Средний")
	obj.gender = int(input("Выбор: "))
	
	print("Падеж")
	print("1.Именительный (Кто? Что?)")
	print("2.Родительный (Кого? Чего?)")
	print("3.Дательный (Кому? Чему?)")
	print("4.Винительный (Кого? Что?)")
	print("5.Творительный (Кем? Чем?)")
	print("6.Предложный (О/В ком? О/В чём?)")
	obj.case = int(input("Выбор: "))
	
	return obj
	
def createVerb():
	obj = Verb()
	
	obj.number = input("Число множественное? (y/n): ") == "y"
	
	print("Род")
	print("1.Мужской")
	print("2.Женскицй")
	print("3.Средний")
	obj.gender = int(input("Выбор: "))
	
	print("Время")
	print("1.Прошедшее")
	print("2.Настоящее")
	print("3.Будущее")
	obj.time = int(input("Выбор: "))
	
	return obj
	

word_dict = {}

with open("dictionary.json", "r") as read_file:
	word_dict = json.load(read_file)

words = input("Введите предложение: ").lower()
words_list = words.split(" ")

for word in words_list:
	if word not in word_dict:
		print()
		print("Встречено неизвестное слово '{}'".format(word))
		answ = input("Заполнить информацию? (y/n): ")
		
		if answ == "y":
			print("Выберите часть речи:")
			print("1.Имя существительное")
			print("2.Глагол")
			print("0.Отмена")
			
			answ = input("Выбор: ")
			
			if answ == "1":
				word_dict[word] = createNoun().toDict()
			elif answ == "2":
				word_dict[word] = createVerb().toDict()
	
if input("Сохранить словарь? (y/n): ") == "y":			
	with open("dictionary.json", "w") as write_file:
		json.dump(word_dict, write_file)

				
			
		
		
