matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
print(matrix[2][1])
numbers = (1,2,3,4,5)
print(numbers)
print(type(numbers))
print(numbers[0])
#numbers[0] = 'unos'
#print(numbers)#arroja error las tuplas son inmutables

############# ---- Juego de Ajedrez    ----- #########
chess_board = [
    ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
    ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
    ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
]

print(chess_board)