import collections, nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
from nltk.tokenize import word_tokenize

def getwords(f, stop, punctuations):
    sens = nltk.sent_tokenize(f.read().lower())
    total = 0
    adj = []
    non = []
    verb= []
    pron= []
    adv = []
    for sen in sens:
        words_list = nltk.pos_tag(nltk.word_tokenize(sen))
	for w, tag in words_list:
	    #print w, tag
	    if w not in punctuations:
		total = total + 1;
                if tag == 'JJ':
		    adj.append(w)
                if tag == 'NN':
		    non.append(w)
                if tag == 'VB':
		    verb.append(w)
                if tag == 'PRP':
		    pron.append(w)
                if tag == 'RB':
		    adv.append(w)
    return total, collections.Counter(non), collections.Counter(verb), collections.Counter(adj), collections.Counter(pron), collections.Counter(adv)

def create_set(f):
    # add stoplist words into a set.splitlines func to remove /r/n
    res = set(f.read().splitlines())
    return res

def write_to_file(non, verb, adj, file):
    f = open(file, 'w')
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
    for i in adj:
	words, count = i
        f.write(str(words)+','+str(count))
        f.write('\n')
	    

if __name__ == '__main__':
    text1 = open('/home/dongchen/Documents/eecs549_HW1/ehr.txt')
    text2 = open('/home/dongchen/Documents/eecs549_HW1/medhelp.txt')
    stoptext = open('/home/dongchen/Documents/eecs549_HW1/stoplist.txt')
    stop = create_set(stoptext);
    punctuations = set(['.', ',', '"', "'", '?', '!', ':', ';', '(', ')', '[', ']', '{', '}', '/', '-', '*', '%', '+', '$', '@', '^', '~', '=', '<', '>'])
    total1, n1, v1, adj1, p1, adv1 = getwords(text1, stop, punctuations)
    total2, n2, v2, adj2, p2, adv2 = getwords(text2, stop, punctuations)
#the top 10 nouns, top 10 verbs, and top 10 adjectives
    write_to_file(n1.most_common(10), v1.most_common(10), adj1.most_common(10), '/home/dongchen/Documents/eecs549_HW1/topTag1.csv')
    write_to_file(n2.most_common(10), v2.most_common(10), adj2.most_common(10), '/home/dongchen/Documents/eecs549_HW1/topTag2.csv')
#percentage of nouns, adjectives, verbs, adverbs, and pronouns
    print total1, sum(n1.values()), sum(adj1.values()), sum(v1.values()), sum(adv1.values()), sum(p1.values())
    print total2, sum(n2.values()), sum(adj2.values()), sum(v2.values()), sum(adv2.values()), sum(p2.values())

