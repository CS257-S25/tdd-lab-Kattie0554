'''
A file for the production code
'''

def reverse_word(word):
    '''
    A function that reverses a word.
    '''
    reverse_word = ""
    for i in range(len(word)-1, -1, -1):
        reverse_word += word[i] 
    return reverse_word

def reverse_all_words(phrase):
    '''
    A function that reverses all the words in a phrase in order.
    '''
    words = phrase.split()
    reversed_words = []
    for word in words:
        reversed_words.append(reverse_word(word))
    return ' '.join(reversed_words)
    
