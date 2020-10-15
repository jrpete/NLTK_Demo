import multiprocessing


class TextClassifier:
  
    def __init__(self):
        pass

    def labelClassifier(self):
        import jsonlines
        import csv
        from nltk.tokenize import word_tokenize

        newsDict = {}
        newsList = []

        '''with jsonlines.open('..\Data\sample.jsonl') as f:
          for line in f.iter():
              #newsDict['text'] = line['text']
              tokenized_text=word_tokenize(line['text'])
              newsDict[line['title']] = line['text']
     
              newsList.append(tokenized_text)
        '''

         
               
        with open('sample.csv', 'wt',  encoding='utf-8') as csvfile:
            fieldnames = ['title', 'text']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, quoting=csv.QUOTE_MINIMAL, escapechar='\\')

            writer.writeheader()

            for k,v in newsDict.items():
              writer.writerow({'title': k, 'text':v.strip()})


    def csvToDF(self):
        import pandas as pd
        file = pd.read_csv("sample.csv")
        file_cleaned = file.dropna().drop_duplicates().reset_index(drop=True)

        return file_cleaned

    def textToWord(self, sentences):
        import re
        
        #sentences['text'] = str(sentences['text']).lower()
        test_list = []
        #print(sentences['text'])

        for w in sentences['text']:
          # Clean the text
          w = w.lower()
          w = re.sub(r"[^A-Za-z0-9^,!?.\/'+]", " ", str(w))
          w = re.sub(r"\+", " plus ", str(w))
          w = re.sub(r",", " ", str(w))
          w = re.sub(r"\.", " ", str(w))
          w = re.sub(r"!", " ! ", str(w))
          w = re.sub(r"\?", " ? ", str(w))
          w = re.sub(r"'", " ", str(w))
          w = re.sub(r":", " : ", str(w))
          w = re.sub(r"\s{2,}", " ", str(w))
          test_list.append(w)
        return test_list

    def wordPhrases(self, sentences):
        from gensim.models.phrases import Phrases, Phraser

        sent = [row for row in sentences]
        phrases = Phrases(sent, min_count=1, progress_per=50000)
        print(phrases)

        bigram = Phraser(phrases)
        sentences = bigram[sent]
        return sentences[1]

    def bagOfWordifier(self, sentences):
        from gensim.models import Word2Vec
        from time import time 

        print(sentences)
        w2v_model = Word2Vec(min_count=3,
                     window=4,
                     size=300,
                     sample=1e-5, 
                     alpha=0.03, 
                     min_alpha=0.0007, 
                     negative=20,
                     workers=multiprocessing.cpu_count()-1)
        start = time()

        w2v_model.build_vocab(sentences, progress_per=50000)

        print('Time to build vocab: {} mins'.format(round((time() - start) / 60, 2)))


tc = TextClassifier()
tc_label = tc.labelClassifier()
tc_read = tc.csvToDF()
tc_word = tc.textToWord(tc_read)
tc_text = tc.wordPhrases(tc_word)
tc_bow = tc.bagOfWordifier(tc_text)
print(tc_bow)

#tc_text = tc.textToWord(tc_label)
#tc_wp = tc.wordPhrases(tc_text)
