from collections import deque

grafo = {
    1: [2],
    2: [1, 3],
    3: [2, 7, 4],
    4: [3, 5, 8],
    5: [4, 6],
    6: [5, 13],
    7: [3, 8],
    8: [4, 7, 9],
    9: [8, 10, 14],
    10: [9, 11],
    11: [10, 12, 15],
    12: [11, 13],
    13: [12, 6],
    14: [9, 15],
    15: [11, 14, 16],
    16: [15, 17, 20],
    17: [16, 18],
    18: [17, 19, 21],
    19: [18, 20],
    20: [16, 19, 55],
    21: [18, 22],
    22: [21, 23],
    23: [22, 24, 28],
    24: [23, 25, 29],
    25: [24, 26],
    26: [25, 27, 30],
    27: [26, 28],
    28: [23, 27, 29],
    29: [24, 28, 30],
    30: [26, 29, 31],
    31: [30, 32],
    32: [31, 33, 36],
    33: [32, 34, 37],
    34: [33, 35],
    35: [34, 36],
    36: [32, 35],
    37: [33, 38, 41],
    38: [37, 39],
    39: [38, 40],
    40: [39],
    41: [37, 42, 43],
    42: [41, 44],
    43: [41, 46],
    44: [42, 45, 47],
    45: [44, 46],
    46: [43, 45, 48],
    47: [44, 49],
    48: [46, 50, 51],
    49: [47, 54],
    50: [48, 52],
    51: [48, 53],
    52: [50, 53],
    53: [51, 52, 54],
    54: [49, 53, 55],
    55: [20, 54, 56],
    56: [55]
}
def bfs(grafo, inicio):
    visitados = set()
    fila = deque([inicio])
    caminho = {inicio: [inicio]}
    
    while fila:
        vertice = fila.popleft()
        
        if vertice not in visitados:
            visitados.add(vertice)
            
            for vizinho in grafo[vertice]:
                if vizinho not in visitados and vizinho not in fila:
                    fila.append(vizinho)
                    caminho[vizinho] = caminho[vertice] + [vizinho]
                    
    return caminho

caminhos = bfs(grafo, 1)
for vertice, caminho in caminhos.items():
    print(f"Vertice {vertice}: Caminho {caminho}")