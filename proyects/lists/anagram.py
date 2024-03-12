def find_anagrams(word, candidates):
    anagrams = []
    letters_word = [letter for letter in word.upper()]
    letters_word.sort()
    for candi in candidates:
        if word.upper() != candi.upper():
            cand_words = [let for let in candi.upper()]
            cand_words.sort()
            if letters_word == cand_words:
                anagrams.append(candi)
    return anagrams

