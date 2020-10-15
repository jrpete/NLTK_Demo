from TextModel import TextModelClass

class TextModelCoreClass:
  
  def getFilePath(self, filepath):
    return TextModelClass.pandasRead(self, filepath)

  def getSentimentPlot(self, files):
    return TextModelClass.sentimentPlot(self, files)

  def getBagOfWords(self, files):
    return TextModelClass.bagOfWords(self, files)

  def getMakeModel(self, files, bow):
    return TextModelClass.makeModel(self, files, bow)

  def getTermFreqIDF(self, files):
    return TextModelClass.termFreqIDF(self, files)

  def getClassificationModel(self, terms):
    return TextModelClass.classificationModel(self, terms)

if __name__ == "__main__":
  #from TextModelCore import TextModelCoreClass
  tm = TextModelCoreClass()

  tm_getFilePath = tm.getFilePath('..\\Data\\financial_news.csv')
  print(tm_getFilePath)

  tm_getSentimentPlot = tm.getSentimentPlot(tm_getFilePath)

  tm_getBagOfWords = tm.getBagOfWords(tm_getFilePath)
  print(tm_getBagOfWords)

  tm_getMakeModel = tm.getMakeModel(tm_getFilePath,tm_getBagOfWords)
  print(tm_getMakeModel)

  tm_getTermFreqIDF = tm.getTermFreqIDF(tm_getFilePath)
  print(tm_getTermFreqIDF)

  tm_getClassificationModel = tm.getClassificationModel(tm_getTermFreqIDF)
  print(tm_getClassificationModel)