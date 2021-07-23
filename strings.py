name = input('Enter:')
print(name)

apple = input('Enter:')
x = apple - 10
#gives traceback as apple is a string
#we solve this issue by converting apple into a integer
x = int(apple) - 10

#[] is a index operator
#inddex value mustbe an integer and start with '0'
fruit = 'banana'
letter = fruit[0]
print(letter)
#it prints 'b'

#index value can be an expression that is computed
x = 3
w = fruit[x - 1]
print(w)

#'len' function gives the length of the string
print(len(fruit))

#LOOPING THROUGH STRINGS
#WAY NO. 1
#using while + len functions togethee we can contruct a loop
#look at each of the letters in a string individually
fruit = 'banana'
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(index, fruit)
    index = index + 1

#WAY NO. 2
fruit = 'banana'
for  letter in fruit:
    print(letter)

#LOOPING AND COUNTING
word = 'banana'
count = 0
for letter in word:
    if letter == 'a'
        count = count + 1
print(count)

#SLICING STRINGS
s = 'Monty Python'
print(s[0:4])

#the second no. is one beyond the end of the slice -
#'upto but not including'
print(s[6:7])

#if the second no. is beyond the string, it stops at th end of the string
print(s[6:20])

#if we leave of the first and the second no. of the slice, it is assumed
#to be the beginning or the ending of the string.
print(s[:2])
print(s[8:])
print(s[:])
