text = 'a aa abC aa ac abc bcd a'
split_text = text.lower().split()  # ['a', 'aa', 'abc', 'aa', 'ac', 'abc', 'bcd', 'a']

def count_words(text):
    word_counts = {word: text.count(word) for word in text}
    # print the dictionary in different lines
    for key, value in word_counts.items():
        print(key, value)

count_words(text.lower().split())

