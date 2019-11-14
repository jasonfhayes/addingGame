## Addition Game

## Establish Constants (Some will update on launch from previous play)
savedScorePath = 'usersScore.txt'
usersScore = 'usersScore.txt'
correctAnswers = 0
incorrectAnswers = 0
pointsEarned = 0
roundNumber = 1

## Import modules
import random
from playAgainFunction import*
from fileReadWrite import *
from gatherSaveData import *
from tellUserHowTheyAreDoing import *


## See if the user has already played before and if so set constants from previous play
savedScoreFound = fileExists(savedScorePath)
if savedScoreFound == True:
    previousGameData = readFile(usersScore)
    gameSaveDataFound = previousGameData
    gameSaveDataFound = gameSaveDataFound.split(',')
    pointsEarned = int(gameSaveDataFound[2])
    roundNumber = int(gameSaveDataFound[3])
    incorrectAnswers = int(gameSaveDataFound[1])
    correctAnswers = int(gameSaveDataFound[0])
    print('Welcome back to the adding game!')
    print('Your current score is:', str(pointsEarned))
    print()
else:
    print('Welcome To The Adding Game')
    print()


## Begin main loop
playAgain = True
while playAgain == True:
    ## Get two random numbers and get their total
    firstValue = random.randrange(-20, 21)
    secondValue = random.randrange(-20, 21)
    sumOffirstValueAndsecondValue = firstValue + secondValue

    ## Print round number
    print('Round', str(roundNumber) + ':')

    ## Ask user to guess the sum
    questionString = str(firstValue) + ' + ' + str(secondValue) + ' = '

    while True:
        usersGuess = input(questionString)
        try:
            usersGuess = int(usersGuess)
            break
        except:
            print('The value you entered is not an integer. Please try again.')
            print()            

    ## Check the answer
    if usersGuess == sumOffirstValueAndsecondValue:
        print('Correct')
        correctAnswers += 1
        pointsEarned += 2
        roundNumber += 1
        tellUserHowTheyAreDoing(correctAnswers, incorrectAnswers, pointsEarned)
        saveData = gatherSaveDataAndJoin(correctAnswers, incorrectAnswers, pointsEarned, roundNumber)
        playAgain = verifyPlayAgain(usersScore, saveData)
    else:
        print('Incorrect')
        incorrectAnswers += 1
        pointsEarned -= 2
        roundNumber += 1
        tellUserHowTheyAreDoing(correctAnswers, incorrectAnswers, pointsEarned)
        saveData = gatherSaveDataAndJoin(correctAnswers, incorrectAnswers, pointsEarned, roundNumber)
        playAgain = verifyPlayAgain(usersScore, saveData)
