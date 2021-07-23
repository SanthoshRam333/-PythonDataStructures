#concatenating lists using '+'
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)

#slicing lists
t = [9, 41, 12, 3, 76, 90]
t[1:3]
t[:4]
t[3:]
t[:]

#building a list from scratch
stuff = list()
stuff.append('book')
stuff.append(99)
print(stuff)

#is something in the list?
some = [9, 41, 12, 3, 76, 90]
9 in some #gives - True
15 in some #gives - False
20 not in some #gives - True

#lists are in Order
friends = [ 'Joseph', 'Glenn', 'Sally']
friends.sort()
print(friends) #gives - [ 'Glenn', 'Joseph', 'Sally']

#built-in functions in lists
nums  = [9, 41, 12, 3, 76, 90, 3, 345, 140]
print(len(nums)) #gives - 6
print(max(nums)) #gives - 345
print(min(nums)) #gives - 3
print(sum(nums)) #gives -
print(sum(nums)/len(nums)) #gives -
