class TextParserClass:

    def fileRead(self, filepath):
        from nltk.tokenize import word_tokenize
        import csv

        newsList = []
        
        with open(filepath, 'rt') as csvfile:
            fieldnames = ['sentiment', 'text']
            
            csvReader = csv.reader(csvfile, delimiter=',', quotechar='"')

            for row in csvReader:
                newsDict = {}
                tokenized_text=word_tokenize(row[1])
                newsDict[row[0]] = tokenized_text
                newsList.append(newsDict)
                
        return newsList


    def findFreqDist(self, sentences):
        from nltk.probability import FreqDist
        word_dist = []

        for row in sentences:
            for k,v in row.items():
                word_dist.append(v)
        
        fdist = FreqDist(word_dist[1])
        return fdist.most_common(5)

    def removeStopWords(self, sentences):
        from nltk.corpus import stopwords

        stop_words=set(stopwords.words("english"))
        filtered_sent=[]


        for row in sentences:
            for key,value in row.items():
                temp_list = []
                temp_dict = {}
                for v in value:
                    if v not in stop_words:
                        temp_list.append(v)
    
                temp_dict[key] = temp_list
                filtered_sent.append(temp_dict)
        
        return filtered_sent


    def wordStemmer(self, sentences):
        from nltk.stem import PorterStemmer

        ps = PorterStemmer()
        stemmed_words=[]
        
        for row in sentences:
            for key,value in row.items():
                temp_list = []
                temp_dict = {}
                for v in value:
                    temp_list.append(ps.stem(v))
    
                temp_dict[key] = temp_list
                stemmed_words.append(temp_dict)
        
        return stemmed_words

    def wordLemmatizer(self, sentences):
        from nltk.stem.wordnet import WordNetLemmatizer
        lem = WordNetLemmatizer()

        lem_words = []
        
        for row in sentences:
            for key,value in row.items():
                temp_list = []
                temp_dict = {}
                for v in value:
                    temp_list.append(lem.lemmatize(v,"v"))
    
                temp_dict[key] = temp_list
                lem_words.append(temp_dict)
        
        return lem_words

    def speechTagger(self, sentences):
        from nltk import pos_tag

        pos_tags = []

        for row in sentences:
            for key,value in row.items():
                temp_list = []
                temp_dict = {}
                
                temp_dict[key] = pos_tag(value)
                pos_tags.append(temp_dict)
        return pos_tags


'''
fr = FileParser()    
fr_read = fr.fileRead()
fr_stop = fr.removeStopWords(fr_read)
fr_stem = fr.wordStemmer(fr_stop)
fr_lem = fr.wordLemmatizer(fr_stop)
fr_pos = fr.speechTagger(fr_stop)

sa = SentimentAnalyzer()
sa_read = sa.pandasRead()
sa_plot = sa.sentimentPlot(sa_read)
sa_bow = sa.bagOfWords(sa_read)
sa_model = sa.makeModel(sa_read, sa_bow)
sa_term = sa.termFreqIDF(sa_read)
sa_class = sa.classificationModel(sa_term)
'''