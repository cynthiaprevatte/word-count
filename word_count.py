# Analyze a text file containing a book for is vocabulary frequency and display the most frequent words to the user in the terminal.

# Download a book as a UTF-8 text file.
# Deal with any decoding errror that arise.
# Normalize words so differences in capitalization and punctuation don't affect counts.
# Count how often each word is used.

# Count how often each unique pair of words is used, then print the most frequent top 10 out with their counts.

# Super Advanced: Allow the user to enter a word and get the most likely words to follow the given word. Store the pair counts as a dict of dicts, where the first key is the first word in the pair and the second key is the second word.

# Enter Query Word > Mr.
# The most likely bi-gram pair starting with "Mr." is "Mr. Darcy".
# Redo the pair counts: normalize the probabilities in the inner dict by the count of pairs that start with the first word.

# Add the ability to generate random sentences, one word at a time, from a given starting word. This is a language model.

# book.txt = 'Jane said, Here, Puff. Come here. Look! said Jane. Look here, Puff. Jane said, Puff!  Puff! Look at this. Come here and look at this.'

import string

word_list = open('book.txt', 'r').read().lower().split(' ')
print(word_list)

# for item in string.punctuation:
#     for word in word_list:
#         if item in word_list:
#             word = word.replace(item, '')

for i in range(len(string.punctuation)):
    for j in range(len(word_list)):
        if string.punctuation[i] in word_list[j]:
            word_list[j] = word_list[j].replace(string.punctuation[i], '')

word_count = {}

word_set = sorted(set(word_list))

for word_s in word_set:
    count = 0
    for word_l in word_list:
        if word_s == word_l:
            count += 1
            word_count[word_s] = count
print(word_count.items())

