""" Analyzes the word frequencies in a book downloaded from
	Project Gutenberg """

import string

def get_word_list(file_name):
	""" Reads the specified project Gutenberg book.  Header comments,
		punctuation, and whitespace are stripped away.  The function
		returns a list of the words used in the book as a list.
		All words are converted to lower case.
	"""
	text = open(file_name,'r')
	Text = text.read()
	start = string.find(Text," ***")
	Text = Text[start+4:]
	end = string.find(Text,"*** ")
	Text = string.lower(Text[:end])
	return string.split(Text)

def get_top_n_words(word_list, n):
	""" Takes a list of words as input and returns a list of the n most frequently
		occurring words ordered from most to least frequently occurring.

		word_list: a list of words (assumed to all be in lower case with no
					punctuation
		n: the number of words to return
		returns: a list of n most frequently occurring words ordered from most
				 frequently to least frequently occurring
	"""
	wcList = {}
	for w in word_list:
		if w not in wcList:
			wcList[w] = word_list.count(w)
	ordered_by_frequency = sorted(wcList, key=wcList.get, reverse=True)
	return ordered_by_frequency[:n]

print get_top_n_words(get_word_list("pg32325.txt"),100)