def reverse(text):
    new = [letter for letter in text]
    new.reverse()
    reverse = ''.join([rev for rev in new])
    return reverse
