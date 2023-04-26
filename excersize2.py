# Create a function that counts how many distinct words are in the string below, then outputs a dictionary with the words as the key and the value as the amount of times that word appears in the string.
# Should output:
# {'a': 5,
# 'abstract': 1,
# 'an': 3,
# 'array': 2, ... etc...

a_text = 'In computing, a "hash" table hash map is a data structure which implements an associative array abstract data type, a structure that can map keys to values. A hash table uses a hash function to compute an index into an array of buckets or slots from which the desired value can be found'

import pprint # Module to format dictionary printing for readablity

def count_words(astring):
    word_count = {}
    words = astring.split()
    for word in words:                         # O(n)-T   /   O(n)-S
        word = word.strip(',.!?$#@%&():;\'\"') # O(n)-T strip linear for time / O(1)-S same memory space regardless of .strip()
        if word in word_count:                 # O(1)-T   /   O(1)-S
            word_count[word] += 1
        else:                                  # O(1)-T   /   O(1)-S
            word_count[word] = 1
    pprint.pprint(word_count)                  # O(n)-T function iterates through dict to format....I think...

count_words(a_text)                            # Time complexity: O(n^2 + n + 1*6) => O(n^2)
                                               # Space complexity: O(n)