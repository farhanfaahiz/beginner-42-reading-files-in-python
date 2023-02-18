fh = open('demo.txt')

print(fh.read())

fh.close

#new example

fh = open('demo.txt')

print(fh.readline())
print(fh.readline())
print(fh.readline())

fh.close

#new example

fh = open('demo.txt')

for line in fh:
    print(len(line.split(' ')))

fh.close

#with open('demo.txt') as fh:
#    for line in fh:
#        print(len(line.split(' ')))