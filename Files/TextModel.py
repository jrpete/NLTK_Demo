class TextModelClass:
  
    def pandasRead(self, filepath):
        import pandas as pd
        data=pd.read_csv(filepath, sep=',', quotechar='"', error_bad_lines=False, engine='python')
        
        return data

    def sentimentPlot(self, data):
        import matplotlib.pyplot as plt

        Sentiment_count=data.groupby('Sentiment').count()
        plt.bar(Sentiment_count.index.values, Sentiment_count['Text'])
        plt.xlabel('Review Sentiments')
        plt.ylabel('Number of Review')
        plt.show()

    def bagOfWords(self, data):
        from sklearn.feature_extraction.text import CountVectorizer
        from nltk.tokenize import RegexpTokenizer

        token = RegexpTokenizer(r'[a-zA-Z0-9]+')
        cv = CountVectorizer(lowercase=True,stop_words='english',ngram_range = (1,1),tokenizer = token.tokenize)
        text_counts= cv.fit_transform(data['Text'])
        
        return(text_counts)

    def makeModel(self, data, text_counts):
        from sklearn.model_selection import train_test_split

        X_train, X_test, y_train, y_test = train_test_split(text_counts, data['Sentiment'], test_size=0.3, random_state=1)

        from sklearn.naive_bayes import MultinomialNB
        #Import scikit-learn metrics module for accuracy calculation
        from sklearn import metrics
        # Model Generation Using Multinomial Naive Bayes
        clf = MultinomialNB().fit(X_train, y_train)
        predicted= clf.predict(X_test)
        return("MultinomialNB Accuracy:",metrics.accuracy_score(y_test, predicted))

    def termFreqIDF(self, data):
        from sklearn.feature_extraction.text import TfidfVectorizer
        tf=TfidfVectorizer()
        text_tf= tf.fit_transform(data['Text'])

        from sklearn.model_selection import train_test_split
        X_train, X_test, y_train, y_test = train_test_split(text_tf, data['Text'], test_size=0.3, random_state=123)

        return X_train, X_test, y_train, y_test

    def classificationModel(self, data):
        from sklearn.naive_bayes import MultinomialNB
        from sklearn import metrics
        # Model Generation Using Multinomial Naive Bayes
        clf = MultinomialNB().fit(data[0], data[2])
        predicted= clf.predict(data[1])
        print("MultinomialNB Accuracy:",metrics.accuracy_score(data[3], predicted))