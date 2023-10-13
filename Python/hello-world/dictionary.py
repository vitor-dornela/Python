dictionary = ['all', 'an', 'and', 'as', 'closely', 'correct', 'equivocal',
              'examine', 'indication', 'is', 'means', 'minutely', 'or', 'scrutinize',
              'sign', 'the', 'to', 'uncertain']
input_phrase = input("Enter your sentence: ")
input_phrase = input_phrase.split()
incorrect_words = []

for i in input_phrase:
    if i not in dictionary:
        incorrect_words.append(i)

if incorrect_words:
    #print("Incorrect words:")
    for word in incorrect_words:
        print(word)
else:
    print("OK")
