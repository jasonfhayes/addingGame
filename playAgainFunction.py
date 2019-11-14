from fileReadWrite import *

def verifyPlayAgain(filePath, dataToWrite):
    playAgain = input('Play again? y or n: ')
    if playAgain == 'y':
        print()
        playAgain = True
        return playAgain
    else:
        print()
        print('Score saved.')
        print('Thanks for playing. Goodbye.')
        writeFile(filePath, str(dataToWrite))
        playAgain = False
        return playAgain
