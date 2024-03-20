# teste - objetivo
# receber entrada 'sample'
# apresentar saída 'plesam'

word = str(input())
letter = str(input())

def magic_mirror():
    magic_happening = word.split(letter)
    magic_happening.append(letter)
    magic_happening = reversed(magic_happening)

    magic_result = str()
    for element in magic_happening:
        magic_result += str(element)

    return magic_result

print(magic_mirror())