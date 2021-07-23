#handle = open(filename, mode)
#returns a handle use to manipulate the file
#filename is a string
#mode is optional, should be 'r' if we want ot read the file, or 'w'
#if we want to write to the file

fhand = open('mbox.txt')
print(fhand)

stuff = 'Hello\nWorld!'
print(stuff)

xfile = open('mbox.txt')
for cheese in xfile:
    print(cheese)

#counting lines in a filename
fhand = open('mbox.txt')
count = 0
for line in fhand:
    count = count + 1
print('Line Count:', count)

#reading the WHOLE file
fhand = open('mbox-short.txt')
inp = fhand.read()
print(len(inp))

print(inp[:20])

#searching through a lines
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rtrip()
    if line.startswith('From:'):
        print(line)

#skipping with continue
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rtrip()
    if line.startswith('From:'):
            continue
        print(line)

#using 'in' to select lines
fhand = fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rtrip()
    if not '@uct.ac.za' in line:
        print(line)

#prompting for filename
fname = input('Enter the file name:')
fhand = open(fname)
count = 0
for line in fhand:
    if line.startswith('Subject:')
        count = count + 1
print('There were', count, 'subject lines in', fname)

#bad file names
fname = input('Enter the file name:')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    quit()

count = 0
for line in fhand:
    if line.startswith('Subject:')
        count = count + 1
print('There were', count, 'subject lines in', fname)
