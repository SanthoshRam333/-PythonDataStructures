#a list is kind of collection
#a 'collection' allows us to put many values in a single 'variable'

friends = [ 'Joseph', 'Glenn', 'Sally']
carryon = [ 'socks', 'shirt', 'perfume']

print(['red', 34, 443 , 2, 89])
print([]) #empty list
print([3, [213, 87], 5, 1]) #list within list

print(friends[1]) #looking inside lists

#lists are mutable
#strings are NOT mutable

lotto = [2, 4, 1, 63, 31, 87, 90]
lotto[2] = 100 #100 replaces 1

print(len(lotto)) #gives 7 as the result

#using the 'range' function
print(range(4)) #gives - [0, 1, 2, 3]

print(range(len(friends))) #gives - [0, 1, 2]

#counted loop
for i in range(len(friends)):
    friend = friends[i]
    print('Happy New Year:', friend)
