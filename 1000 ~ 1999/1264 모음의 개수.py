while True:
    sentence = input()
    if(sentence == '#'):
        break
    sentence = sentence.lower()
    print(sentence.count('a') + sentence.count('e') + sentence.count('i') + sentence.count('o') + sentence.count('u'))