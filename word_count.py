# Write a module to analyze a text file containing a book for is vocabulary frequency and display the most frequent words to the user in the terminal.

# Find a book on Project Gutenberg. Download it as a UTF-8 text file.

# Open the file and deal with any decoding errror that arise.

# Normalize all of the words so differences in capitalization and punctuation attached to words don't affect the counts.

# Count how often each unique word is used, then print the most frequent top 10 out with their counts.

# Count how often each unique pair of words is used, then print the most frequent top 10 out with their counts.

# Advanced

# Make a command line tool with the sys.argv. Allow the the user to pass in the filename to a .txt file when execiting your program. Use the sys.argv to parse the filename to use for the analysis.
# Super Advanced

# Allow the user to enter a word and get the most likely words to follow the given word. Store the pair counts as a dict of dicts, where the first key is the first word in the pair and the second key is the second word.

# Enter Query Word > Mr.
# The most likely bi-gram pair starting with "Mr." is "Mr. Darcy".
# Redo the pair counts: normalize the probabilities in the inner dict by the count of pairs that start with the first word.

# Chain together that ability to generate random sentences, one word at a time, from a given starting word. This is a language model.

# sentence = "Find a book on Project Gutenberg. Download it as a UTF-8 text file. Open the file and deal with any decoding errror that arise. Normalize all of the words so differences in capitalization and punctuation attached to words don't affect the counts. Count how often each unique word is used, then print the most frequent top 10 out with their counts. Count how often each unique pair of words is used, then print the most frequent top 10 out with their counts"

import re
#p = re.compile(r'''
import string
#string.punctuation

with open('text.txt', 'r') as file:
    word_list = file.readline()

word_list = word_list.split(' ')
word_count = {}

punctuation = '['+string.punctuation+']'

for word in word_list:
    re.sub(punctuation, '', word)

# for i in range(len(string.punctuation)):
#     for j in range(len(word_list)):
#         if string.punctuation[i] in word_list[j]:
#             word_list[j] = word_list[j].replace(string.punctuation[i], '')

for word in word_list:
    word = word.lower()

# for i in range(len(word_list)):
#     for j in range(len(word_count)):
#         if word_list[i] in word_count:
#             new_word_count = word_count[j][1]
#             del word_count[j]

print(word_list)

# pattern = '['+string.punctuation+']'
# re.sub('{$'.format(pattern), '', phrase)

