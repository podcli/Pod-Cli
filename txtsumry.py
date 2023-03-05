import re
import nltk
import heapq
nltk.download('punkt')
nltk.download('stopwords')
transcribed =  open('/mnt/32F6E6CAF6E68D83/kaam/FOSS/PODCLI/Assemblyai/assemblyai-and-python-in-5-minutes/transcript.txt', "r")
data = transcribed.read()
transcribed.close()
#raw text taken as input which is fetched from database.
raw_text=data
raw_text.lower()
#preprocessing
# removing spaces,puntations and numbers
clean_text=re.sub('[^a-zA-Z]',' ',raw_text)
clean_text=re.sub('\s+',' ',clean_text)
#print(clean_text+'\n')
#split into sentence list
sentence_list=nltk.sent_tokenize(raw_text)
#print(sentence_list)
#word frequency
stopwords=nltk.corpus.stopwords.words('english')
word_frequencies={}
for word in nltk.word_tokenize(clean_text):
    if word not in stopwords:
        if word not in word_frequencies:
            word_frequencies[word]=1
        else:
            word_frequencies[word]+=1
maximum_frequency=max(word_frequencies.values())
for word in word_frequencies:
    word_frequencies[word]= word_frequencies[word]/maximum_frequency
#calculate sentence scores
sentence_scores={}
for sentence in sentence_list:
    for word in nltk.word_tokenize(sentence):
        if word in word_frequencies and len(sentence.split(' ')) < 100000:
            if sentence not in sentence_scores:
                sentence_scores[sentence]=word_frequencies[word]
            else:
                sentence_scores[sentence]+=word_frequencies[word]
#print(word_frequencies)
#print(sentence_scores)
#get top 5 sentence
summary=heapq.nlargest(350,sentence_scores,key=sentence_scores.get)
print(" ".join(summary)) 
