#"Dictionaries" are like bags - No Order
#So, we index the things we put in the dictionary with a 'lookup tag'
purse = dictionary()
purse ['money'] = 12
purse ['candy'] = 3
purse ['tissue'] = 75
print(purse)
print(purse['candy'])

#dictionary is mutable
purse['candy'] = purse['candy'] + 2

#you can make an 'empty dictionary' using empty curly braces
jj = {'chuck':1, 'fredd':53, 'jan':100}
print(jj)
oo = { }
print(oo)

#we can use in operator to see if a key is in the dictionary
'csev' in purse

#COUNTING WITH DICTIONARIES
#when we see a new name we need to add a new entry in the dictionary
counts = dictionary()
names = ['csev', 'cwen', 'zqian', 'cwen', 'csev']
for name in names:
    if name is not in counts
        counts[name] = 1
    else:
        counts[name]  = counts[name] + 1
    print(counts)

#simplified counting with 'Get'
counts = dictionary()
names = ['csev', 'cwen', 'zqian', 'cwen', 'csev']
for name in names:
    counts[name] = counts.get(name, 0) + 1
print(counts)

#Counting patterns
counts = dictionary()
line = input('Enter a line of text:')
words = line.split()

print('Words', words)
print('Counting...')

for word in words:
    counts[word] = counts.get(word, 0) + 1
print('Counts to:', counts)

#retriving lists of Keys and Values
pp = {'chuck':1, 'fredd':53, 'jan':100}
print(list(pp))

print(pp.keys())

print(pp.values())

print(pp.items())

#Two Iteration Variables
jj = {'chuck':1, 'fredd':53, 'jan':100}
for k,v in jj.items():
    print(k, v)

#counting most words in a file
name = input('Enter the file name:')
handle = open(name)

counts = dictionary()
for line in handle:
    words = line.split()
    for word in words:
            counts[word] = counts.get(word, 0) + 1

bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)
