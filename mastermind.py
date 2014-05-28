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
	
def getWords(length, numberOfWords):
	dictionary 	= getDictionary()
	dictLen 		= len(dictionary)
	words 			= []

	while (len(words) < numberOfWords):
		randomInt 		= random.randint(0, dictLen - 1)
		randomWord 	= dictionary[randomInt]
		
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
		"output" 		: "",
		"nCorrect" 	: 0
	}
	
	for i in range(0, len(word)):
		if word[i] == compareWord[i]:
			matchInfo['output'] += compareWord[i]
			matchInfo['nCorrect'] += 1
		else:
			matchInfo['output'] += "-"	
		
	return matchInfo
	
def results(matchInfo, wordLength):
	print "(" + str(matchInfo['nCorrect']) + "/" + str(wordLength) + " correct) " + matchInfo['output']
	print "" 
			
	if (matchInfo['nCorrect'] == wordLength):
		return True
	else:
		return False
		
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
	nWords 			= 10
	guessesLeft 	= 4
	wordLength 	= getWordLength()
	words 			= getWords(wordLength, nWords)
	guessWord 		= words[random.randint(0, len(words) - 1)]
	
	showWords(words)
	
	while (guessesLeft > 0):
		guess = getGuess(guessesLeft)
		
		if results(matchLetters(guess, guessWord), wordLength):
			win()
			break
		
		guessesLeft -= 1
		
		if (guessesLeft == 0):
			lose()

if __name__ == "__main__":
	main()