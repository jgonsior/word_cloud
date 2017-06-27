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
#text = open(path.join(d, 'constitution.txt')).read()
text = "hallo hallo hallo hallo hallo hallo hallo test test ich ich du er sie es wir ihr sie und was soll ich dann nun tun?"
# Generate a word cloud image
wordcloud = WordCloud().generate(text)

with open("test.htm", "w") as file:
    file.write(wordcloud.to_html())

wordcloud.to_file("test.png")
