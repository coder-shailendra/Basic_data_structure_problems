str=("apple,apple,banana,grapes,orange,cherry")
words = str.split()   # split into list of words

freq = {}

for w in words:
    freq[w] = freq.get(w, 0) + 1

print(freq)