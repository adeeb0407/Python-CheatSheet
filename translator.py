def translate(word):
    translatedValue = "";
    
    for letter in word:
        if letter.lower() in "aeiou":

            if letter.isupper():
                translatedValue += "G"
            else:
                translatedValue += "g"

        else:
            translatedValue += letter
    
    return translatedValue;

print(translate(str(input("Please Enter The Word :"))))
