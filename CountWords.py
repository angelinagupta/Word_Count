intro = input("Enter your introduction.")
print(intro)

wordCount= 1
characterCount = 0

for character in intro: 
    characterCount= characterCount+1
    if(character == ' '):
        wordCount= wordCount+1
print("number of words in string")
print(wordCount)
print("number of characters in string")
print(characterCount)