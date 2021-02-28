def counting_words(text):
    return len(text.split(" "))


def word_count(text):
    print(text)
    word_frequencies=[]
    words_list=text.split()
    for word in words_list:
        word_frequencies.append(words_list.count(word))
    print(word_frequencies)
    return word_frequencies