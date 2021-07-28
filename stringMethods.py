phrase = 'yummy pAncakes taste good'

#gives length of string
print(len(phrase))

upperCase = phrase.upper()  #saving this into a variable just to play around with syntax a bit
print(upperCase)

print(phrase.lower())

#capitalizes the first letter of each word
print(phrase.title())

print(phrase)

#find index of first occurance of char
print(phrase.find('g'))

#returns '-1'
print(phrase.find('x'))

spellcheck = phrase.replace('A', 'a')
print(spellcheck)

#returns boolean
print('good' in phrase)         #True
print('pancakes' in phrase)     #False