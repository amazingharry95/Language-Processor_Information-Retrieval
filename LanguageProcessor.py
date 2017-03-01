from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from sklearn.feature_extraction.text import TfidfVectorizer
from collections import Counter

class LanguageProcessor:
	factory = StemmerFactory()
	stemmer = factory.create_stemmer()
	def __init__(self, pathFile, language):
		self.fileText = open(pathFile, 'r').read()
		self.tokenizeFile = word_tokenize(self.fileText.lower())
		self.language = language.lower()
		self.stopWords = []
		print "Text Original: ", self.fileText

	def setStopWords(self):
		if self.language == "english":
			self.stopWords = set(stopwords.words("english"))
		elif self.language == "indonesia":
			self.stopWords = open("stopWordIndonesia.txt", "r").read().splitlines()
		else:
			print "Sorry :( Doesn't recognize your language!"

	def removeStopWords(self):
		LanguageProcessor.setStopWords(self)
		filteredSentence = [w for w in self.tokenizeFile if not w in self.stopWords]

		return filteredSentence

	def stemmingWords(self, inputan):
		if self.language == "indonesia":
			return LanguageProcessor.stemmer.stem(inputan)
		elif self.language == "english":
			ps = PorterStemmer()
			hasilStem = []
			textInput = inputan.split(' ')

			for w in textInput:
				hasilStem.append(ps.stem(w).encode('utf-8'))

			return hasilStem

	def longestWord(self, inputan):
		sortedWords = sorted(inputan, key=len)

		return sortedWords[-1]

	def frequentWord(self, inputan):
		wordCounts = Counter(inputan)

		return wordCounts

	def assignWeight(self, inputan):
		doc1 = open('contohDokumenIndonesia1.txt', 'r').read()
		doc2 = open('contohDokumenIndonesia2.txt', 'r').read()
		doc3 = open('contohDokumenIndonesia3.txt', 'r').read()
		inputs = list(set(inputan.split(' ')))
		vectorizer = TfidfVectorizer(vocabulary=inputs,decode_error='ignore')
		return vectorizer.fit_transform([doc1, doc2, doc3]).toarray()