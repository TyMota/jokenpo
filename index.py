import random
from time import sleep

print("====================")
print("Vamos jogar JOKENPO?")
print("====================")

lista = ["PEDRA", "PAPEL", "TESOURA"]
final = ""
continuar = ""
historico = ""
empate = 0
computador = 0
voce = 0

bot_choice = random.choice(lista)


player_choice = input("""As opções são:
Pedra
Papel
Tesoura
Digite sua escolha: """).upper()

while player_choice not in ["PEDRA", "PAPEL", "TESOURA"]:
    player_choice = input("""Opção invalidad! As opções são:
Pedra
Papel
Tesoura 
Digite sua escolha: """).upper()
  
print("JO...")
sleep(1)
print("KEN...")
sleep(1)
print("PÔ!!!")
sleep(0.5)

    

def jokenpo_result(player_choice, bot_choice):
    if bot_choice == "PEDRA" and player_choice == "PAPEL":
        final = "venceu"
    elif bot_choice == "PEDRA" and player_choice == "TESOURA":
        final = "perdeu"
    elif bot_choice == "PAPEL" and player_choice == "PEDRA":
        final = "perdeu"
    elif bot_choice == "PAPEL" and player_choice == "TESOURA":
        final = "venceu"
    elif bot_choice == "TESOURA" and player_choice == "PEDRA":
        final = "venceu"
    elif bot_choice == "TESOURA" and player_choice == "PAPEL":
        final = "perdeu"
    else:
        final = "empatou"

    mensagem = (f"Você escolheu {player_choice} e o computador {bot_choice}. Você {final}!")

    return mensagem, final

while continuar != "NAO":

    bot_choice = random.choice(lista)

    msg, final = jokenpo_result(player_choice, bot_choice)

    print(msg)

    if final == "venceu":
        voce += 1
    elif final == "perdeu":
        computador += 1
    elif final == "empatou":
        empate += 1

    continuar = input("Deseja continuar jogado? Digite [SIM] ou [NAO]: ").upper()
    while continuar not in ["SIM", "NAO"]:
        continuar = input("Opção errada! Digite [SIM] ou [NAO]: ").upper()

    if continuar == "SIM":
        player_choice = input("""As opções são:
Pedra
Papel
Tesoura
Digite sua escolha: """).upper()
    else:
        break
    
    while player_choice not in ["PEDRA", "PAPEL", "TESOURA"]:
        player_choice = input("""Opção invalida! As opções são:
Pedra
Papel
Tesoura 
Digite sua escolha: """).upper()
            

print("Fim do Programa!")
print(f"Você venceu {voce} vezes, o computador {computador} vezes e empatou {empate} vezes.")
        