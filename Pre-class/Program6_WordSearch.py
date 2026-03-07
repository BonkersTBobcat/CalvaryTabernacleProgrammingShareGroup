from collections import deque

filename = "./kjv.txt"
target = "Jesus"
window = 30

# stores previous 30 words
prev_words = deque(maxlen=window)

def word_stream(file):
    for line in file:
        for w in line.split():
            yield w

with open(filename, "r", encoding="utf-8") as f:
    stream = word_stream(f)

    for word in stream:
        if target.lower() in word.lower():

            before = list(prev_words)

            after = []
            for _ in range(window):
                try:
                    next_word = next(stream)
                    after.append(next_word)
                    prev_words.append(next_word)
                except StopIteration:
                    break

            snippet = before + [word] + after
            print(" ".join(snippet))
            print("-" * 60)

        prev_words.append(word)