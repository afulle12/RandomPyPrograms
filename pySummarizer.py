#https://www.youtube.com/watch?v=z4DQYprjPSs&list=PL7yh-TELLS1G9mmnBN3ZSY8hYgJ5kBOg-&index=5

import tkinter as tk
import nltk
from newspaper import Article
nltk.download('punkt')

url = 'https://www.aljazeera.com/news/2023/9/12/a-new-and-terrifying-world-kim-and-putin-to-meet-again-in-russia'

article1 = Article(url)
article1.download()
article1.parse()

article1.nlp()

print(f'Title: {article1.title}')
print(f'Authors: {article1.authors}')
print(f'Publication Date: {article1.publish_date}')
print(f'Summary: {article1.summary}')
