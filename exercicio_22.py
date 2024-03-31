print("Escreva um programa que simule um relógio digital usando o módulo `datetime`.\n")

from datetime import datetime
import time

def relogio_digital():
    while True:
        agora = datetime.now()
        hora_formatada = agora.strftime(f"%H:%M:%S")
        print(hora_formatada, end="\r")
        time.sleep(1)
        
relogio_digital()
