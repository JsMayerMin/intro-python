#1
years_list = [1980,1981,1982,1983,1984]
print(years_list)

#2
years_list[2]
print(years_list[2])

#3
print(years_list[0])

#4
things = ['mossarella','cinderella','salmonella']
print(things)

#5
print(things[1].capitalize())
print(things)

#6
print(things[0].swapcase())
print(things)

#7
del things[2]
print(things)

#8
surprise = ["Groucho", "Chico", "Harpo"]

#9
print(surprise[2].lower()[::-1].capitalize())

#10
f2e = {'dog': 'chien', 'cat': 'chat', 'walrus': 'morse'}
print(f2e)

#11
print(f2e['walrus'])

#12
e2f_list = []
for (a,b) in f2e.items():
    e2f_list.append((b, a))
e2f = dict(e2f_list)
print(e2f)

#13
print(e2f['chien'])

#14
print(e2f.keys())

#15
life = {
    'animals' : {'cats' : 'Henri', 'octopi' : 'Grumpy', 'emus' : 'Lucy'},
    'plants' : {},
    'other' : {}
}

#16
print(life.keys())

#17
print(life['animals'].keys())

#18
print(life['animals']['cats'])

