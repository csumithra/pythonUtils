#Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically.

# Suppose the following input is supplied to the program:

# New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
# Then, the output should be:

# 2:2
# 3.:1
# 3?:1
# New:1
# Python:5
# Read:1
# and:1
# between:1
# choosing:1
# or:2
# to:1

from collections import defaultdict

freq = defaultdict(int)

data = input("Enter a string to test word frequency: ")
word_list = data.split(" ")
print(word_list)

for each_word in word_list:
    freq[each_word] += 1

k = sorted(freq.keys())

for k in sorted(freq.keys()):
    print(f'{k}: {freq[k]}')



