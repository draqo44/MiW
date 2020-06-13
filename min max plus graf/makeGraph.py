# Mariusz Olszewski

"""
 f. generująca do pliku kod grafu dla GraphViz
 wygenerowany kod można zwizualizować
 wystarczy skopiować zawartosć pliku i wkleić na stronie
 http://www.webgraphviz.com/


funkcja genGraph generuje graph od konca od lisci,
po to zeby na wyższych poziomach mozna bylo ustalic najlepszy wynik
dla protagonisty max, dla antagonisty min,
poszczegolne wpisy są dodawane do listy graph,
na końcu lista jest odwracana i zapisywana do pliku o nazwie filename
"""


def genGraph(onTable, path, player):
    """ onTable - suma żetonów na stole
        path - jakie żetony na stole
        player -1/+1 - który gracz ma ruch
        1 - protagonista, -1 - antagonista
    """
    # parametry gry (mozna zadać też inne)
    maxOnTable = 21         # ilosć oznaczająca koniec gry
    coin = [4, 5, 6]        # rodzaj żetonów
    players = " PA"         # jednoliterowe skróty graczy
            
    pathExp = "+".join(list(path)) # generuje wyrażenie z położonych żetonów
    
    # koniec gry przekroczono limit - gracz player przegrywa
    # generuje liscie grafu
    if onTable > maxOnTable:
        result = (-1)**(len(path)%2)
        resultStr = "+" + str(result) if result > 0 else str(result)
        leaf = f"\"{players[player]};\\n na stole: {pathExp}={onTable};\\n wynik={resultStr}\" [label = \"koniec;\\n wynik={resultStr}\"];"
        graph.append(leaf)
        return result
    
    # koniec gry osiągnięto limit - remis
    # generuje liscie grafu
    if onTable == maxOnTable:
        result = 0
        leaf = f"\"{players[player]};\\n na stole: {pathExp}={onTable};\\n wynik={result}\" [label = \"koniec;\\n wynik={result}\"];"
        graph.append(leaf)
        return result
    
    # rekurencja i zebranie rezultatów do allRes
    allRes = []
    for c in coin:
        allRes.append(genGraph(onTable + c, path + str(c), -player))
    
    # wynik dla graczy protagonista max, antagonista min
    if player == 1:
        result = max(allRes)
    else:
        result = min(allRes)

    # generowanie węzłów i krawędzi dla danego poziomu
    resultStr = "+" + str(result) if result > 0 else str(result)
    parent = f"\"{players[player]};\\n na stole: {pathExp}={onTable};\\n wynik={resultStr}\" -> "
    
    coin.reverse()
    allRes.reverse()
    for i in range(len(coin)):
        resultStr = "+" + str(allRes[i]) if allRes[i] > 0 else str(allRes[i])
        pathExp = "+".join(list(path + str(coin[i])))
        child = f"\"{players[-player]};\\n na stole: {pathExp}={onTable + coin[i]};\\n wynik={resultStr}\""
        label = f" [label = \"{str(coin[i])}\"];"
        graph.append(parent + child + label)
       
    return result

filename = "graph21.txt"

graph = []      
genGraph(0, "", 1)

outFile = open(filename, 'w')
print("digraph G {\n", file=outFile)

graph.reverse()
for line in graph:
    print(line, file=outFile)

print("\n}", file=outFile)

outFile.close()
