from TextParser import TextParserClass
#source NLPenv/Scripts/activate

class TextParserCoreClass:

  def getFilePath(self, filepath):
    return FileParser.fileRead(self, filepath)

  def getFreqDist(self, files):
    return FileParser.findFreqDist(self, files)

  def getStopWords(self, files):
    return FileParser.removeStopWords(self, files)

  def getWordStems(self, files):
    return FileParser.wordStemmer(self, files)

  def getWordLems(self, files):
    return FileParser.wordLemmatizer(self, files)

  def getPartSpeechTags(self, files):
    return FileParser.speechTagger(self, files)

if __name__ == "__main__":
    cr = TextParserCoreClass()
    cr_getFilePath = cr.getFilePath('..\\Data\\financial_news.csv')
    cr_getFreqDist = cr.getFreqDist(cr_getFilePath)
    cr_getStopwords = cr.getStopWords(cr_getFilePath)
    cr_getWordStems = cr.getWordStems(cr_getStopwords)
    cr_getWordLems = cr.getWordLems(cr_getStopwords)
    cr_getPartSpeechTags = cr.getPartSpeechTags(cr_getStopwords)
