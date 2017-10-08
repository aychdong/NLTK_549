import math, collections, nltk
nltk.download('punkt')
from nltk.stem.porter import *
from nltk.tokenize import word_tokenize

def tf(word, count):
    return math.log(1+(count[word]*1.0 / sum(count.values())))

def n_containing(word, count_list):
    return sum(1 for count in count_list if word in count)

def idf(word, count_list):
    #print len(count_list) / (1 + n_containing(word, count_list))
    return 1+math.log(1.0*len(count_list) / n_containing(word, count_list))

def tfidf(word, count, count_list):
    return tf(word, count) * idf(word, count_list)

def stem_tokens(tokens, stemmer):
    stemmed = []
    for item in tokens:
        stemmed.append(stemmer.stem(item))
    return stemmed

def getwords(line, stop):
    sens = nltk.sent_tokenize(line)
    words = []
    stemmer = PorterStemmer()
    for sen in sens:
        words_in_sen = nltk.word_tokenize(sen)
        words.extend(stem_tokens([word for word in words_in_sen if word not in stop], stemmer))
    return collections.Counter(words)

def create_set(f):
    # add stoplist words into a set.splitlines func to remove /r/n
    res = set(f.read().splitlines())
    return res

def constructCounter(f, stop):
    counter_list = []
    for i, line in enumerate(f.readlines()):
        counter = getwords(line.lower(), stop)
        counter_list.append(counter)
    #print len(counter_list)
    return counter_list

def calculate(countlist):
    for i, count in enumerate(countlist):
        if i>=10:
            break
        print("Top words in document {}".format(i + 1))
        scores = {word: tfidf(word, count, countlist) for word in count}
        sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        for word, score in sorted_words[:5]:
            print("\tWord: {}, TF-IDF: {}".format(word, round(score, 5))) 

if __name__ == '__main__':
    stoptext = open('/home/dongchen/Documents/eecs549_HW1/stoplist.txt')
    stop = create_set(stoptext);
    punctuations = set(['.', ',', '"', "'", '?', '!', ':', ';', '(', ')', '[', ']', '{', '}', '/', '-', '*', '%', '+', '$', '@', '^', '~', '=', '<', '>'])
    stop = stop.union(punctuations)
    text = open('/home/dongchen/Documents/eecs549_HW1/ehr.txt')
    calculate(constructCounter(text, stop))
	
    
