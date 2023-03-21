import getpass as gp
import random

def getPlayerMove(player):
        while True:
            move = gp.getpass(f"{player}, wybierz swój ruch (papier/kamień/nożyce): ").lower()
            if move in ["papier", "kamień", "nożyce"]:
                    return move
            else:
                print("Niepoprawny ruch, spróbuj ponownie!")

def getWinner(player1, player1_move, player2, player2_move):
    if player1_move == player2_move:
        print("Remis")
        return None
    elif (player1_move == "papier" and player2_move == "kamień") or \
         (player1_move == "nożyce" and player2_move == "papier") or \
         (player1_move == "kamień" and player2_move == "nożyce"):
        print(f"{player1} wygrał(a) rundę!")
        return player1
    else:
        print(f"{player2} wygrał(a) rundę!")
        return player2

def roundResults(round_num, player1, player1_move, player2, player2_move, winner):
    print(f"Runda {round_num}: {player1} ({player1_move}) vs {player2} ({player2_move})", end="")
    if winner is not None:
        print(f" - wygrał(a) {winner}")
    else:
        print(" - remis")

def finalResults(player1, player2, player1_wins, player2_wins):
    print("=" * 40)
    print("Wyniki końcowe:")
    print(f"{player1}: {player1_wins} pkt")
    print(f"{player2}: {player2_wins} pkt")
    if player1_wins > player2_wins:
        print(f"{player1} wygrał(a) grę!")
    elif player2_wins > player1_wins:
        print(f"{player2} wygrał(a) grę!")
    else:
        print("Remis!")

print("Witaj w grze 'papier, kamień nożyce'!")
num_rounds = int(input("Podaj liczbę rund: "))
mode = input("Wybierz tryb gry (komputer / 2 graczy): ").lower()
if mode == "komputer":
    player1 = input("Podaj swoje imię: ")
    player2 = "komputer"
else:
    player1 = input("Podaj imię pierwsze gracza: ")
    player2 = input("Podaj imię drugiego gracza: ")

print(f"Rozpoczynamy grę! {player1} vs {player2}")
player1_wins = 0
player2_wins = 0

for i in range(1, num_rounds + 1):
        print(f"Runda: {i}")
        if mode == "komputer":
            player1_move = getPlayerMove(player1)
            player2_move = random.choice(["papier", "kamień", "nożyce"])
        else:
            player1_move = getPlayerMove(player1)
            player2_move = getPlayerMove(player2)

        round_winner = getWinner(player1, player1_move, player2, player2_move)

        if round_winner == player1:
            player1_wins += 1
        elif round_winner == player2:
            player2_wins += 1

        roundResults(i, player1, player1_move, player2, player2_move, round_winner)

finalResults(player1, player2, player1_wins, player2_wins)