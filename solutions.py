def reverse_words(text):
    texts = text.split(' ')
    texts = [textss[::-1] for textss in texts]
    texts = ' '.join(texts)
    return texts
