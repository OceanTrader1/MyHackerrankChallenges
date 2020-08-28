from collections import Counter

def checkMagazine(magazine, note):
    if (Counter(note) - Counter(magazine))=={}:
        print('Yes')
    else:
        print('No')
    return not (Counter(note) - Counter(magazine))