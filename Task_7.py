print("welcome")

word = input("Enter a word: ")

count = 0

for ch in word.lower():
    if ch in "aeiou":
        count += 1

print("Number of vowels:", count)