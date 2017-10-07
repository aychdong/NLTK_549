import collections, nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize

def getwords(f, stop, punctuations):
    sens = nltk.sent_tokenize(f.read())
    upper_count = 0;
    total_count = 0;
    words_count = 0;
    for sen in sens:
        words_list = nltk.word_tokenize(sen)
	for w in words_list:
	    if w not in punctuations:
		upper_count = upper_count + sum(1 for c in w if c.isupper())
                total_count = total_count + len(w)
                words_count = words_count +1
    return upper_count, total_count, words_count

def create_set(f):
    # add stoplist words into a set.splitlines func to remove /r/n
    res = set(f.read().splitlines())
    return res

if __name__ == '__main__':
    text1 = open('/home/dongchen/Documents/eecs549_HW1/ehr.txt')
    text2 = open('/home/dongchen/Documents/eecs549_HW1/medhelp.txt')
    stoptext = open('/home/dongchen/Documents/eecs549_HW1/stoplist.txt')
    stop = create_set(stoptext);
    punctuations = set(['.', ',', '"', "'", '?', '!', ':', ';', '(', ')', '[', ']', '{', '}', '/', '-', '*', '%', '+', '$', '@', '^', '~', '=', '<', '>'])
    s1, t1, w1 = getwords(text1, stop, punctuations)
    s2, t2, w2 = getwords(text2, stop, punctuations)
    print s1, t1, w1
    print s2, t2, w2

