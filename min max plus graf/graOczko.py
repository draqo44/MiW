# Mariusz Olszewski


"""
funkcja oczkoMiniMax przegląda graf wszystkich rozwinięć gry,
po to zeby ustalic najlepszy wynik dla rozpoczynającego grę protagonisty
na poszczególnych poziomach z dostępnych rozwiązań wybierany jest
dla protagonisty max, a dla antagonisty min,
poszczegolne ruchy są dodawane do łańcucha moves,
na końcu zwracana jest wynik i zapis poszczególnych ruchów
"""

def oczkoMiniMax(onTable, path, player):
    """ onTable - suma żetonów na stole
        path - jakie żetony na stole
        player -1/+1 - który gracz ma ruch
        1 - protagonista, -1 - antagonista
    """
    # parametry gry (mozna zadać też inne)
    maxOnTable = 21          # ilosć oznaczająca koniec gry
    coin = [4, 5, 6]         # rodzaj żetonów
            
    # koniec gry przekroczono limit - gracz player przegrywa
    if onTable > maxOnTable:
        return player, ""
    
    # koniec gry osiągnięto limit - remis
    if onTable == maxOnTable:
        return 0, ""
    
    # wybór najlepszego rozwiązania dla gracza: protagonista max, antagonista min
    if player == 1:
        result = -2
        for c in coin:
            res, mov = oczkoMiniMax(onTable + c, path + str(c), -player)
            if res > result:
                result = res
                moves = str(c) + mov
    else:
        result = +2
        for c in coin:
            res, mov = oczkoMiniMax(onTable + c, path + str(c), -player)
            if res < result:
                result = res
                moves = str(c) + mov

    # zwrócenie wyniku
    return result, moves

result, moves = oczkoMiniMax(0, "", 1)

movesPrint = " ".join(list(moves))

print(f"Wynik: {result}")
print(f"Ruchy (protagonista zaczyna): {movesPrint}")

