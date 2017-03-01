import LanguageProcessor as lp
import operator

ownProcessor = lp.LanguageProcessor('Artikel/POL_SK_03_425.txt', 'indonesia')

hasilRemoveStopWords = ownProcessor.removeStopWords()
print "\n\nRemove Stop Words: ", hasilRemoveStopWords

print "Hasil Remove Stop Words: ", ' '.join(hasilRemoveStopWords)

hasilStemming = ownProcessor.stemmingWords(' '.join(hasilRemoveStopWords))
print "\nStemming Sentence: ", hasilStemming

masukanKata = raw_input('\nMasukkan keyword: ')

hasilVectorize = ownProcessor.assignWeight(masukanKata)
print "Weights: ", hasilVectorize
jumlahWeight = [sum(i) for i in hasilVectorize]
jumlahDokumen = list(range(len(jumlahWeight)))
print "Sum of Weights: ", jumlahWeight
dictDokumenWeight = dict(zip(jumlahDokumen, jumlahWeight))
sortedDict = sorted(dictDokumenWeight.items(), key=operator.itemgetter(1), reverse=True)
print "Rank: ", sortedDict

hasilTerpanjang = ownProcessor.longestWord(hasilRemoveStopWords)
print "\nKata terpanjang: ", hasilTerpanjang

hasilCount = ownProcessor.frequentWord(hasilRemoveStopWords)
print "\nHasil Counter: ", hasilCount

print hasilCount[0]
print hasilCount[1]
