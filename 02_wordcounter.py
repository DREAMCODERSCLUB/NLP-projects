import re
from collections import Counter

# Sample input text
text = """
Natural Language Processing (NLP) is a fascinating field of AI.
It helps machines understand human language. Language is power!
"""

# Step 1: Clean the text
text = text.lower()
text = re.sub(r'[^a-z\s]', '', text)

# Step 2: Tokenize (split into words)
words = text.split()

# Step 3: Count word frequencies
word_counts = Counter(words)

# Step 4: Display top 10 words
print("🔝 Top Words:")
for word, count in word_counts.most_common(10):
    print(f"{word}: {count}")
