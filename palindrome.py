prom = input('Write a word: ')
promrev = prom[::-1]

i = 0
m = 0
while i < prom.__len__():
    if prom[i] == promrev[i]:
        i+=1
    else:
        print('Not this word')
        break

if i == prom.__len__():
    print('this word: ' + prom)
