import os
import shutil
import time


def cleanname(name):
    forbidden_chars = ['\\', '/', ':', '*', '?', '"', '<', '>', '|']
    for char in forbidden_chars:
        name = name.replace(char, '')
    return name


index = 0
total = -1
letras = []


with open('lyrics.txt', 'r') as f:
    for line in f:
        total += 1
        letras.append(line.strip())
    for line in letras:
        print(index, ' ', total)
        if index <= total:
            print(index, '<', total)
            os.mkdir(cleanname(letras[index]))
            print(letras[index])

        if index == total:
            print(index, '=', total)
            print(os.system('dir'))
            with open(letras[index], 'w') as file:
                file.write(letras[index])
            print('rmdir ' + '"' + letras[index] + '"')
            os.system('rmdir ' + '"' + cleanname(letras[index]) + '"')
        if index <= total:
            os.chdir(cleanname(letras[index]))
        index += 1

print(letras)
time.sleep(10000000)
