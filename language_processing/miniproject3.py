
from pattern.web import *
def main():
	text = open('./pg42.txt','r')
	JHText = text.read()
	words = []
	word = ''
	letters = []
	for i in range(65,91):
		letters.append(chr(i))
	for i in range(97,123):
		letters.append(chr(i))
	for let in JHText:
		if let in letters or let == "'":
			word += let
		elif word:
			if len(word) > 0:
				words.append(word)
			word = ''
	#print words
	Lword = ''
	for w in words:
		if len(w) > len(Lword):
			Lword = w
	print "Longest Word:",Lword
	wcList = {}
	for w in words:
		if w in wcList:
			wcList[w] += 1
		else:
			wcList[w] = 1
	mostWordList = []
	mostWordListNoNum = []
	for i in range(len(wcList)):
		mostWord = ''
		mostWordNum = 0
		for w in wcList.keys():
			if wcList[w] > mostWordNum and w not in mostWordListNoNum:
				mostWord = w
				mostWordNum = wcList[w]
		mostWordList.append([mostWord, mostWordNum])
		mostWordListNoNum.append(mostWord)
	for i in range(1,51):
		print "Word #%d:" % i,
		print "%s, appears" % mostWordListNoNum[i-1],
		print "%d times" % mostWordList[i-1][1]
main()