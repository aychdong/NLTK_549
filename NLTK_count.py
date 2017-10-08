import collections, nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize

def getwords(f):
    sens = nltk.sent_tokenize(f.read().lower())
    words = []
    for sen in sens:
        words.extend(nltk.word_tokenize(sen))
    return collections.Counter(words)

def write_to_file(words, stop, punctuations, file):
    f = open(file, 'w')
    numStops = 0
    for i in words:
        #for j in i:
            #f.write(str(j)+',')
        words, count = i
        if words not in punctuations:
            if words not in stop:
                f.write(str(words)+','+str(count))
                f.write('\n')
	    else:
	        numStops = numStops + count
    return numStops
	    

def write_to_file_set(words, file):
    f = open(file, 'w')
    for i in words:
        f.write(str(words))
        f.write('\n')

def create_set(f):
    # add stoplist words into a set.splitlines func to remove /r/n
    res = set(f.read().splitlines())
    return res

if __name__ == '__main__':
    text1 = open('/home/dongchen/Documents/eecs549_HW1/ehr.txt')
    text2 = open('/home/dongchen/Documents/eecs549_HW1/medhelp.txt')
    stoptext = open('/home/dongchen/Documents/eecs549_HW1/stoplist.txt')
    words1 = getwords(text1)
    words2 = getwords(text2)
    stop = create_set(stoptext);
    punctuations = set(['.', ',', '"', "'", '?', '!', ':', ';', '(', ')', '[', ']', '{', '}', '/', '-', '*', '%', '+', '$', '@', '^', '~', '=', '<', '>', '...', '&', '|', '#', '\'\'','``',  '~'])
    #stop = stop.union(punctuations)
    write_to_file_set(stop, '/home/dongchen/Documents/eecs549_HW1/stoplist_check.txt')
    print write_to_file(words1.most_common(), stop, punctuations, '/home/dongchen/Documents/eecs549_HW1/results1.csv')
    print write_to_file(words2.most_common(), stop, punctuations, '/home/dongchen/Documents/eecs549_HW1/results2.csv')
