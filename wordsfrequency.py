import sys
import codecs
import nltk
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
# NLTK's default German stopwords

def topwords(renoted_id):


    default_stopwords = set(nltk.corpus.stopwords.words('english'))

# We're adding some on our own - could be done inline like this...
# ... but let's read them from a file instead (one stopword per line, UTF-8)
#stopwords_file = './stopwords.txt'
#custom_stopwords = set(codecs.open(stopwords_file, 'r', 'utf-8').read().splitlines())

#all_stopwords = default_stopwords | custom_stopwords
    all_stopwords = default_stopwords
    filepath="alldocs/processed/"+renoted_id+".txt"


    fp = codecs.open(filepath, 'r', 'utf-8')

    words = nltk.word_tokenize(fp.read())

# Remove single-character tokens (mostly punctuation)
    words = [word for word in words if len(word) > 1]

# Remove numbers
    words = [word for word in words if not word.isnumeric()]

# Lowercase all words (default_stopwords are lowercase too)
    words = [word.lower() for word in words]

# Stemming words seems to make matters worse, disabled
# stemmer = nltk.stem.snowball.SnowballStemmer('german')
# words = [stemmer.stem(word) for word in words]
# Remove stopwords
    words = [word for word in words if word not in all_stopwords]

###lemmetize words
    lmtzr = WordNetLemmatizer()
   # port = PorterStemmer()
    words = [lmtzr.lemmatize(word) for word in words ]
   # words = [port.stem(word) for word in words ]
# Calculate frequency distribution
    fdist = nltk.FreqDist(words)
    retdict=[]
    topwords={}

# Output top 50 words

    for word, frequency in fdist.most_common(50):
        if len(word)>3:
            value= {"word":word,"frequency":frequency}
            retdict.append(value)
    topwords["topwords"]=retdict
    return topwords
        #print(u'{};{}'.format(word, frequency))
