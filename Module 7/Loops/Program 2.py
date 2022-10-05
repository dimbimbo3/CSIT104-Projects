userStr = input("Enter a string:")

strVowels = ""

for ch in userStr:
    if ch in "aeiou":
        strVowels += ch
    elif ch in "AEIOU":
        strVowels += ch

print("The vowels are " + strVowels)
