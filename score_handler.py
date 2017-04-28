
def getHighScore():
    try:
        scores = []
        file_object = open('./high_score.txt', 'r')
        previous_scores = file_object.readlines()
        file_object.close()
        for lines in previous_scores:
            scores.append(int(lines))

        scores.sort(reverse = True)
        return scores[0]

    except:
        file_object = open('high_score.txt', 'w')
        file_object.write('0')
        file_object.close()
        return getHighScore()

def setHighScore(score):
    if score > getHighScore():
        file_object = open('high_score.txt', 'w')
        file_object.write(str(score))
        file_object.close()
        




