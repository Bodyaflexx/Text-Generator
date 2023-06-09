import random
import re
import nltk
from nltk.tokenize import WhitespaceTokenizer
from collections import Counter


def start_word_add():
    pattern = r'^[A-Z][^\.\!\?]*$'
    while True:
        word = random.choice(tokens)
        if re.match(pattern, word):
            chain.append(word)
            break


def common_word_add():
    pattern = r'^[a-zA-Z]+(?:[-\'][a-zA-Z]+)*$'
    while True:
        last_word = chain[-1]
        tail_list = list(d[last_word].keys())
        freq_list = list(d[last_word].values())
        next_word = random.choices(tail_list, weights=freq_list)[0]
        if len(chain) > 5 and last_word_check(next_word):
            chain.append(next_word)
            return True
        if re.match(pattern, next_word):
            chain.append(next_word)
            break


def last_word_check(word):
    pattern = r'^.*[.?!]$'
    if re.match(pattern, word):
        return True


file_path = input()
with open(file_path, "r", encoding="utf-8") as f:
    s = f.read()
tokenizer = WhitespaceTokenizer()
tokens = tokenizer.tokenize(s)
unique_tokens = set(tokens)
bigrams = list(nltk.bigrams(tokens))
d = {}
for group in bigrams:
    d.setdefault(group[0], Counter())
    d[group[0]].setdefault(group[1], 0)
    d[group[0]][group[1]] += 1
for i in range(10):
    chain = []
    start_word_add()
    while True:
        if common_word_add():
            break
    print(" ".join(chain))
