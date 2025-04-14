def count_words(sentence):
    words = sentence.split()
    return len(words)

text = "hello im student"
print("단어 수:", count_words(text))