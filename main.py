from yellowbrick.datasets import load_hobbies
from yellowbrick.text.correlation import word_correlation
from yellowbrick.datasets import load_concrete
import pandas as pd

# Load the text corpus
corpus = load_hobbies()

# Create the list of words to plot
words = [ "home", "picnic", "barbecue", "movie", "lunch", "dinner", "swim",
          "school", "church", "hiking", "football", "basketball",
          "office", "banana", "meat", "wine", "soda", "water", "ice cream", "cake",
          "chicken", "breakfast", "vegetable", "cereal"]

# Draw the plot
word_correlation(words, corpus.data)
