sentence = input("Input sentence :")
words = letters = numbers = 0
punctuation = [".", ";", " ", ","]
dict = {}

sentence.strip()
sentence = " ".join(sentence.split())
print(sentence)

for ch in sentence :
    if(ch == " "):
        words += 1
    if ch.isalpha() :
        letters += 1
        if ch not in dict.keys():
            dict[ch] = 1
        else:
            dict[ch] += 1    
    elif ch.isnumeric():
        numbers += 1
        if ch not in dict.keys():
            dict[ch] = 1
        else:
            dict[ch] += 1 

words += 1            
print("Words : ", words)
print("Letters : ", letters)
print("Numbers : ", numbers)            
print(dict)