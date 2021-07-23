#'Split' breaks a string into parts and produce a list of strings
abc = 'With three words'
stuff = abc.split()
print(stuff)
print(len(stuff)) #gives - 3
print(stuff[0]) #gives - With

for w in stuff:
    print(w)

line = 'first;second;third'
thing = line.split(;)
print(thing)

fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rtrip()
    if not line.startswith('From:'):
            continue
    words= line.split()
        print(line)

#double split pattern
words = line.split()
email = words[1]
pieces = email.split('@')
print(pieces[1]) #gives - uct.ac.za
