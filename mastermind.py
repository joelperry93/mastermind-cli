import random

def main():
	title()
	play()
	
def getDictionary():
	words = []

	with open('./enable1.txt') as file:
		for line in file:
			words.append(line.strip())
	
	return words

def getWordLength():
	return int(raw_input("How many characters will the word have? "))

def getGuess(guessesLeft):
	return raw_input("Guess? (" + str(guessesLeft) + " left): ")

def getRandomElement(list):
	return list[random.randint(0, len(list) - 1)]
	
def getWords(length, numberOfWords):
	dictionary 	= getDictionary()
	words 		= []

	while (len(words) < numberOfWords):
		randomWord = getRandomElement(dictionary)
		
		if (len(randomWord) == length):
			words.append(randomWord)
			
	return words

def showWords(words):
	print ""
	print "Guess the word:"
	
	for word in words:
		print word
		
	print ""
	
def matchLetters(word, compareWord):
	matchInfo = {
		"output" 	: "",
		"nCorrect" 	: 0
	}
	
	for i in range(0, len(word)):
		if word[i] == compareWord[i]:
			matchInfo['output'] += compareWord[i]
			matchInfo['nCorrect'] += 1
		else:
			matchInfo['output'] += "-"	
		
	return matchInfo
	
def results(matchInfo):
	print "(" + str(matchInfo['nCorrect']) + "/" + str(len(matchInfo['output'])) + " correct) " + matchInfo['output']
	print "" 
			
	if (matchInfo['nCorrect'] == len(matchInfo['output'])):
		return True #win
	else:
		return False #lose
		
def win():
	print "Well done! You got it!"
	print ""
	
def lose():
	print "Sorry, you lose."
	print ""

def title():
	print "Mastermind Pro Edition 2014"
	print "---------------------------"

def play():
	guessesLeft 	= 4
	words 		= getWords(getWordLength(), 10)
	guessWord 		= getRandomElement(words)
	
	showWords(words)
	
	while (guessesLeft > 0):
		guess = getGuess(guessesLeft)
		
		if results(matchLetters(guess, guessWord)):
			win()
			break
		
		guessesLeft -= 1
		
		if (guessesLeft == 0):
			lose()

if __name__ == "__main__":
	main()