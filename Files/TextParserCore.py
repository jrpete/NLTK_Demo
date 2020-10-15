from TextParser import TextParserClass

class TextParserCoreClass:

  def getFilePath(self, filepath):
    return TextParserClass.fileRead(self, filepath)

  def getFreqDist(self, files):
    return TextParserClass.findFreqDist(self, files)

  def getStopWords(self, files):
    return TextParserClass.removeStopWords(self, files)

  def getWordStems(self, files):
    return TextParserClass.wordStemmer(self, files)

  def getWordLems(self, files):
    return TextParserClass.wordLemmatizer(self, files)

  def getPartSpeechTags(self, files):
    return TextParserClass.speechTagger(self, files)

if __name__ == "__main__":
    #source NLPenv/Scripts/activate
    #from TextParserCore import TextParserCoreClass
    cr = TextParserCoreClass()

    cr_getFilePath = cr.getFilePath('..\\Data\\financial_news.csv')
    print(cr_getFilePath)

    cr_getFreqDist = cr.getFreqDist(cr_getFilePath)
    print(cr_getFreqDist)

    cr_getStopwords = cr.getStopWords(cr_getFilePath)
    print(cr_getStopwords)

    cr_getWordStems = cr.getWordStems(cr_getStopwords)
    print(cr_getWordStems)

    cr_getWordLems = cr.getWordLems(cr_getStopwords)
    print(cr_getWordLems)

    cr_getPartSpeechTags = cr.getPartSpeechTags(cr_getStopwords)
    print(cr_getPartSpeechTags)
