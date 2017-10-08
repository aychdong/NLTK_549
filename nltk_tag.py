import collections, nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
from nltk.tokenize import word_tokenize

def getwords(f, stop, punctuations):
    sens = nltk.sent_tokenize(f.read().lower())
    adj = []
    non = []
    verb= []
    pron= []
    for sen in sens:
        words_list = nltk.pos_tag(nltk.word_tokenize(sen))
	for w, tag in words_list:
	    #print w, tag
	    if w not in punctuations:
		if tag == 'JJ':
		    adj.append(w)
                if tag == 'NN':
		    non.append(w)
                if tag == 'VB':
		    verb.append(w)
                if tag == 'PRP':
		    pron.append(w)
    return collections.Counter(adj), collections.Counter(non), collections.Counter(verb), collections.Counter(pron)

def create_set(f):
    # add stoplist words into a set.splitlines func to remove /r/n
    res = set(f.read().splitlines())
    return res

def write_to_file(adj, non, verb, porn, file):
    f = open(file, 'w')
    for i in adj:
	words, count = i
        f.write(str(words)+','+str(count))
        f.write('\n')
    f.write('\n')
    for i in non:
	words, count = i
        f.write(str(words)+','+str(count))
        f.write('\n')
    f.write('\n')
    for i in verb:
	words, count = i
        f.write(str(words)+','+str(count))
        f.write('\n')
    f.write('\n')
    for i in porn:
	words, count = i
        f.write(str(words)+','+str(count))
        f.write('\n')
	    

if __name__ == '__main__':
    text1 = open('/home/dongchen/Documents/eecs549_HW1/ehr.txt')
    text2 = open('/home/dongchen/Documents/eecs549_HW1/medhelp.txt')
    stoptext = open('/home/dongchen/Documents/eecs549_HW1/stoplist.txt')
    stop = create_set(stoptext);
    punctuations = set(['.', ',', '"', "'", '?', '!', ':', ';', '(', ')', '[', ']', '{', '}', '/', '-', '*', '%', '+', '$', '@', '^', '~', '=', '<', '>'])
    s1, t1, w1, p1 = getwords(text1, stop, punctuations)
    s2, t2, w2, p2 = getwords(text2, stop, punctuations)
    write_to_file(s1.most_common(10), t1.most_common(10), w1.most_common(10), p1.most_common(10), '/home/dongchen/Documents/eecs549_HW1/topTag1.csv')
    write_to_file(s2.most_common(10), t2.most_common(10), w2.most_common(10), p2.most_common(10), '/home/dongchen/Documents/eecs549_HW1/topTag2.csv')

