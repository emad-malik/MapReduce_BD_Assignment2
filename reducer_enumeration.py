#!/usr/bin/env python3
import sys

current_word = None
current_count = 0
word = None
word_id = 0

# Input comes from standard input (stdin)
for line in sys.stdin:
    # Parse the input we got from mapper.py
    line = line.strip()

    # Split the line into word and count, which are separated by a tab
    word, count = line.split('\t', 1)

    # Convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        continue

    
    if current_word == word:
        current_count += count
    else:
        if current_word:
            # Write result to standard output (stdout)
            print(f'{current_word}\t{word_id}\t{current_count}')
            word_id += 1
        current_count = count
        current_word = word

if current_word == word:
    print(f'{current_word}\t{word_id}\t{current_count}')
