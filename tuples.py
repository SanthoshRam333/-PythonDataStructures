#tuples are like lists
x = ('Joseph', 'Glenn', 'Sally')
print(x[2])

y = (1, 9, 0)
print(max(y))

#TUPLES ARE NOT MUTABLE
#you can also put a tuple on the left-hand side
(x, y) = (4, 'Freedom')
print(y)

(a, b) = (99, 93)
print(a)

#TUPLES ARE COMPARABLE
(0, 1, 2) < (5, 2, 8)
(9, 4, 3267823) < (9, 641, 234234)
('Jones', 'Sally') < ('Jones', 'Sam')
('Jones', 'Sally') > ('Adam', 'Sam')

#usiing sorted()
d = {'a':1, 'c':100, 'b':53}
t = sorted(d.items())
t

for k,v in sorted(d.items()):
    print(k, v)

#sort by values instead of key
c = {'a':10, 'b':1, 'c':22}
tmp = list()
for k, v in c.items():
    tmp.append((v, k))
tmp = sorted(tmp, reverse = True)
print(tmp)

#find the top most 10 common words
fhand = open('romeo.txt')
counts = dictionary()
for line in handle:
    words = line.split()
    for word in words:
            counts[word] = counts.get(word, 0) + 1

lst = list()
for key, val in counts.items():
    newtup = (value, key)
    tmp.append(newtup)

lst = sorted(lst, reverse = True)

for val, key in lst[:10]:
    print(key, val)

#List Comprehension
c = {'a':1, 'c':100, 'b':53}
print(sorted([(v, k) for k, v in c.items()]))\
