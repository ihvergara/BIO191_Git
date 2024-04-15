
# VERGARA, IVYANN ROMIJN H. 
# 2020-00761

# ================= Seatwork 3.4 =================
mystring = input("\nEnter a word: ")
vowels = 'aeiouy'

# Count the number of vowel groups.
count = 0
is_vowel = False
for char in mystring:
  if char in vowels:
    if not is_vowel:
      count += 1
    is_vowel = True
  else:
    is_vowel = False
# A mystring with zero vowels or ending in "e" has 1 syllable. 
if count == 0 or (mystring[-1] == 'e' and len(mystring) > 1):
  count = 1

if count == 1:
  print(mystring+": " + str(count) +" syllable")
else:
  print(mystring+": " + str(count) +" syllables")
