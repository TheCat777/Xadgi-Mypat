import time
import os


def stop():
  print("Для продолжения введите любой текст")
  a = input()

  
print('Добро пожаловать в квестовый квест:')
time.sleep(1)
print('Хаджи-Мурат. Альтернативные истории')
time.sleep(1)
while True:
	print('Вы готовы начать играть? Да/Нет')
	a = input()
	if a == "да":
		stop()
	elif a == "нет":
		break
	else:
		print('Неккорктный ввод')
os.system("clear")
