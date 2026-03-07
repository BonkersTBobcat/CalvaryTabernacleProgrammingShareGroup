# Import deque from collection library
from collections import deque

filename = "Program6_kjv.txt"
target = "healing"
window = 30

# create deque
previous_words = deque(maxlen=window)

def word_stream(file):
    for line in file:
        for w in line.split():
            yield w

# open file
with open(filename, "r", encoding="utf-8") as f:
    # create word stream
    stream = word_stream(f)
    # loop through all words in stream
    for word in stream:
        # if current word is the target word, print it
        if target.lower() in word.lower():
            before = list(previous_words)
            after = []
            # find the next 30 word
            for _ in range(window):
                try:
                    next_word = next(stream)
                    after.append(next_word)
                    previous_words.append(next_word)
                except StopIteration:
                    break
            # print finding
            snippet = before + [word] + after
            print(" ".join(snippet))
            print("-" * 60)
        # after processing, add this word to the previous words list
        previous_words.append(word)