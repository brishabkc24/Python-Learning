"""Take parts of a string with slicing: [start:stop:step].

Run: python 02_slicing.py
"""

word = "programming"
print("Word:", word)
print("Indexes: 0 1 2 3 4 5 6 7 8 9 10")

# [start:stop] gives the characters from start up to, but not including, stop.
print("word[0:3]  ->", word[0:3])
print("word[3:7]  ->", word[3:7])

# Leaving out start means "from the beginning"; leaving out stop means
# "to the end".
print("word[:4]   ->", word[:4])
print("word[4:]   ->", word[4:])
print("word[:]    ->", word[:])

# Negative positions work in slices too.
print("word[-4:]  ->", word[-4:])
print("word[:-4]  ->", word[:-4])

# The third number is the step: how many characters to jump each time.
print("word[::2]  ->", word[::2])
print("word[1::2] ->", word[1::2])

# A step of -1 walks backwards, which reverses the string.
print("word[::-1] ->", word[::-1])

# A stop beyond the end is not an error; the slice just stops at the end.
print("word[5:50] ->", word[5:50])

# Slicing is useful for real data such as dates and file names.
date_text = "2024-06-15"
print()
print("Year:", date_text[:4])
print("Month:", date_text[5:7])
print("Day:", date_text[8:])

file_name = "report_final.pdf"
print("Extension:", file_name[-3:])
print("Name only:", file_name[:-4])
