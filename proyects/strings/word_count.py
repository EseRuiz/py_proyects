import re
def count_words(sentence):
    regex = r"[^\w']+"
    new_sentence = sentence.split('_')
    clean_sentence = ' '.join(new_sentence).lower()
    clean_sentence = re.sub(regex, ' ', clean_sentence.lower().strip("'"))
    new_word = clean_sentence.strip().split(' ')
    new_word2 = []
    for word in new_word:
        if word.startswith("'") and word.endswith("'"):
            new_word2.append(word[1:len(word)-1])
        elif word.startswith("'"):
            new_word2.append(word[1:])
        elif word.endswith("'"):
            new_word2.append(word[:-1])
        else:
            new_word2.append(word)
    dict_words = {word: new_word2.count(word) for word in new_word2 if word != ''}
    return (dict_words)

a = count_words("Joe can't tell between 'large' and large.")
print(a)
{'joe': 1, "can't": 1, 'tell': 1, 'between': 1, "large'": 1, 'and': 1, 'large': 1}
{"joe": 1, "can't": 1, "tell": 1, "between": 1, "large": 2, "and": 1}