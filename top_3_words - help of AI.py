from collections import Counter
def top_three_words(text):
    text_str=""
    for char in text:
        if char.isalpha() or char==" ":
            text_str+=char.lower()
    words = text_str.split(" ")
    count = Counter(words)
    return [word for word, freq in count.most_common(3)]
text = input()
result = top_three_words(text)
print(result)
