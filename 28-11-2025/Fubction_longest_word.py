def find_longest_word(sentence):
    words = sentence.split()
    longest_word = max(words, key=len)#here what i saw is max is comparing between words in string and how by takign length as kry
    return longest_word

# Example usage:
sentence = "The quick brown fox jumps over the lazy dog"
print(find_longest_word(sentence)) 
