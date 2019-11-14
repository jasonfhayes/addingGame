def gatherSaveDataAndJoin(correctAnswers, incorrectAnswers, pointsEarned, roundNumber):
    listOfDataToSave = [str(correctAnswers), str(incorrectAnswers), str(pointsEarned), str(roundNumber)]
    saveDataString = ','.join(listOfDataToSave)
    return saveDataString
