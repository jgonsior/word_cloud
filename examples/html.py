#!/usr/bin/env python
"""
Minimal Example
===============

Generating a square wordcloud from the US constitution using default arguments.
"""
from pprint import pprint
from os import path
from wordcloud import WordCloud
d = path.dirname(__file__)

# Read the whole text.
text = open(path.join(d, 'constitution.txt')).read()
# Generate a word cloud image
wordcloud = WordCloud().generate(text)

print(wordcloud.to_html())

import matplotlib.pyplot as plt
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")

#plt.show()
