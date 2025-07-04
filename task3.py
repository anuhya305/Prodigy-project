# -*- coding: utf-8 -*-
"""Task3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1_CMfZpjLvQe-isFU4JEkoFtk-LBSD7Bm
"""

# 📌 Step 1: Sample Input Text
sample_text = """
Once upon a time in a land far away, there lived a king and a queen.
The king was kind and wise, and the queen was graceful and brave.
Together, they ruled the kingdom in peace and happiness.
"""

# 📌 Step 2: Build the Markov Chain
def build_markov_chain(text, n=1):
    words = text.split()
    chain = {}

    for i in range(len(words) - n):
        key = tuple(words[i:i+n])
        next_word = words[i+n]
        if key not in chain:
            chain[key] = []
        chain[key].append(next_word)

    return chain

# 📌 Step 3: Generate Text
import random

def generate_text(chain, length=30):
    key = random.choice(list(chain.keys()))
    result = list(key)

    for _ in range(length):
        next_words = chain.get(key)
        if not next_words:
            break
        next_word = random.choice(next_words)
        result.append(next_word)
        key = tuple(result[-len(key):])

    return ' '.join(result)

# 📌 Step 4: Run the Model
chain = build_markov_chain(sample_text, n=1)
generated_text = generate_text(chain, length=30)
print("Generated Text:\n")
print(generated_text)