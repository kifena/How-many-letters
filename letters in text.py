import sys

first = 0
last = 0

for i in range(0,10000):
    if chr(i) == 'А':
        first = i
    elif chr(i) == 'я':
        last = i
        break
alphabet=[]

for i in range(first,last+1):
    alphabet.append(chr(i))

for i in range(0,10000):
    if chr(i) == 'Ё':
        first = i
    elif chr(i) == 'ё':
        last = i


alphabet.append(chr(first))
alphabet.append(chr(last))

for i in range(len(alphabet)):
    if alphabet[i]=='Е':
        first=i
    elif alphabet[i]=='е':
        last=i

a=alphabet.pop(alphabet.index('Ё'))
b=alphabet.pop(alphabet.index('ё'))

alphabet.insert(first+1,a)
alphabet.insert(last+1,b)

f = open(sys.argv[1], "r")
text=f.read()

counter={}
summa=0
print('Всего символов - %d из них пробелов - %d' %(len(text),text.count(' ')))
print()
for letter in alphabet:
    n=text.count(letter)
    if n!=0:
        counter[letter]=n
for letter in counter:
    summa=summa+counter[letter]
    print ("%s - %s" % (letter, counter[letter]))
    
print ('Всего русских букв -',summa)

