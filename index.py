import random
from time import sleep

print("====================")
print("Vamos jogar JOKENPO?")
print("====================")

lista = ["PEDRA", "PAPEL", "TESOURA"]
final = ""

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
    
msg, resultado = jokenpo_result(player_choice, bot_choice)
print(msg)

        