def nextGreatestLetter(letters, target):
    for ch in letters:
        if ch > target:
            return ch
    return letters[0]
letters = ['c', 'f', 'j']
target = 'd'
print(nextGreatestLetter(letters, target))
