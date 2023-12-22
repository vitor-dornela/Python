import re

text = "This is a sample text with a specific word. Another specific word in the text."

word_to_find = "specific"

matches = re.findall(r'\b' + re.escape(word_to_find) + r'\b', text)

count = len(matches)

print(f"The word '{word_to_find}' appears {count} times in the text.")