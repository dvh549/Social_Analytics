import pickle

import nltk
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
import preprocessor as p

def preprocess(text):
    text = p.clean(text)
    tokenization = nltk.word_tokenize(text)     
    tokenization = [w for w in tokenization if not w in stop_words]   
    return text

def load_vectorizer():
    vectorizer = pickle.load(open("models/misinformation/vectorizer.txt", "rb"))
    return vectorizer

def load_misinformation_model():
    logreg_filename = "models/misinformation/logreg.txt"
    logreg = pickle.load(open(logreg_filename, 'rb'))
    return logreg

def fake_or_real(pred):
    if pred == 0:
        return "Real"
    else:
        return "Fake"
    
if __name__ == "__main__":
    text_to_check = "The CDC currently reports 99031 deaths. In general the discrepancies in death counts between different sources are small and explicable. The death toll stands at roughly 100000 people today."
    logreg, vectorizer = load_misinformation_model(), load_vectorizer()
    text_to_check_vectorized = vectorizer.transform([preprocess(text_to_check)])
    print(fake_or_real(logreg.predict(text_to_check_vectorized)[0])) # Actual label: Real