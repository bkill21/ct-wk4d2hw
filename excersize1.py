# Reverse the list below in-place using an in-place algorithm.
# For extra credit: Reverse the strings at the same time.

words = ['this' , 'is', 'a', 'sentence', '.']

def rev_list(alist):
    output = []
    left, right = 0, len(alist) - 1
    while left < right:    #Loop to reverse word order of list
        alist[left], alist[right] = alist[right], alist[left]
        left += 1
        right -= 1

    for word in alist:   #Loop to reverse letter order of words for extra credit :)
        unpacked_word = [*word]
        left, right = 0, len(word) - 1
        while left < right:
            unpacked_word[left], unpacked_word[right] = unpacked_word[right], unpacked_word[left]
            left += 1
            right -= 1
        rev_word = ''.join(unpacked_word)
        output.append(rev_word)
        
    return output              
        
rev_list(words)
print(words)