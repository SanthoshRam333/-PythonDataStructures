# '+' means 'concatenation'
a = 'Hello'
b = a + "There"
print(b)

c = a + ' ' + 'There'
print(c)

#USING 'IN' AS A LOGICAL OPERATOR
#'in' returns 'True' or 'False'
fruit = 'banana'
'n' in fruit
'm' in fruit
'nan' in fruit

if 'a' in fruit:
    print('Found it!')

#STRING COMPARISON

if word == 'banana':
print('All right, bananas.')

if word < 'banana':
    print('Your word,' + word + ', comes before banana')

if word > 'banana':
    print('Your word,' + word + ', comes after banana')

#STRING LIBRARY

great = 'Hello Bob'
zap = great.lower()
print(zap)

print('Hi There'.lower())

nn = great.upper()
print(nn)

#searching a string
pos = fruit.find('na')
print(pos)

#'-1' is reurned as there is no 'm' in th estring
aa = fruit.find('m')
print(aa)

greet = 'Hello Bob'
new = greet.replace('Bob', 'Jane')
print(new)

new2 = greet.replace('o', 'X')
print(new2)

#stripping whitespace
greet = '      Hello Bob  '
greet.lstrip() #gives - 'Hello Bob  '
greet.rstrip() #gives - '     Hello Bob'
greet.strip() #gives - 'Hello Bob'

#prefixes
line = 'Please have a nice day'
line.startswith('Please') #gives True
line.startswith('P') #gives False

#PARSING AN EXTRACTING
data = 'From stephen.maple@uct.ac.za Sat Jan 5 09::13:22 2017'
atpos = data.find('@') #gives the position - 21
spos = data.find(' ', atpos) #gives the position - 31
host = data[atpos+1 : spos]
print(host) #gives - uct.ac.za
