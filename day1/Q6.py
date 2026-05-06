# Count the frequency of each character in a string using a dictionary.


freq = {}

for ch in s:
    if ch in freq:
        freq[ch] += 1
    