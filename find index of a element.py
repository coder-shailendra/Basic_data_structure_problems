def find_index(t, key):
    for i in range(len(t)):
        if t[i] == key:
            return i
    return -1

print(find_index((10,20,30,40), 30))
