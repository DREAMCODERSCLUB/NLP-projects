import re
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from collections import defaultdict, Counter

nltk.download('punkt')  # Download tokenizer models
nltk.download('punkt_tab')  # Download tokenizer models

# Sample text
text = """
Natural Language Processing is a part of artificial intelligence.
It deals with the interaction between computers and humans using natural language.
The ultimate goal of NLP is to read, decipher, understand, and make sense of human languages in a manner that is valuable.
Most NLP techniques rely on machine learning to derive meaning from human languages.
NLP is used in a variety of applications such as chatbots, translation, and sentiment analysis.
"""

# Step 1: Clean and tokenize
text_clean = re.sub(r'[^a-zA-Z\s]', '', text)
words = word_tokenize(text_clean.lower())
sentences = sent_tokenize(text)

# Step 2: Create word frequency table (excluding stopwords)
stopwords = nltk.corpus.stopwords.words('english')
word_freq = Counter(word for word in words if word not in stopwords)

# Step 3: Score sentences based on word frequencies
sentence_scores = defaultdict(int)

for sentence in sentences:
    for word in word_tokenize(sentence.lower()):
        if word in word_freq:
            sentence_scores[sentence] += word_freq[word]

# Step 4: Select top N sentences
top_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:2]

# Step 5: Display summary
print("📝 Summary:\n")
for sent in top_sentences:
    print("-", sent)
