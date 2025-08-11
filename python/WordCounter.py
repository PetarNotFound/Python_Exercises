sentence = input("Enter a sentance: ")

words = sentence.split()
word_count = len(words)
space_count = sentence.count(" ")
longest_word = max(words, key=len)

print(f"Word count: {word_count}")
print(f"Character count (with spaces): {len(sentence)}")
print(f"Character count (with spaces): {int(len(sentence)) - int(space_count)}")
print(f"Longest word: {longest_word}")
