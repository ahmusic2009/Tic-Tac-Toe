# Test Commit
places = ['1','2','3','4','5','6','7','8','9']

def board():
    print (places[0] +'|' +places[1] + '|' +places[2])
    print ('-----')
    print (places[3] +'|' +places[4] + '|' +places[5])
    print ('-----')
    print (places[6] +'|' +places[7] + '|' +places[8])

#Game Title

print('Welcome to Tic-Tac-Toe!')
print('')
board()
print('')

#Game Play

turns = 0

while turns < 4:
    i = int(input('Player x: Where would you like to make your move?'))
    places[i-1] = 'x'
    print('')
    board()

    i = int(input('Player o: Where would you like to make your move?'))
    turns += 1
    places[i-1] = 'o'
    print('')
    board()

#Final turn
i = int(input('Player x: Where would you like to make your move?'))
places[i-1] = 'x'
print('')
board()

#Game over

if places[0] == places[1] == places[2]:
    print(places +'wins!')

    print('Game over, thanks for playing!')
