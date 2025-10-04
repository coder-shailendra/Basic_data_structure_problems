str=input("enter the str:")
vowels=("a,e,i,o,u,A,E,I,O,U")
v_count=0
c_count=0
for ch in str:
    if ch.isalpha():   # check if character is a letter
        if ch in vowels:
            v_count += 1
        else:
            c_count += 1

print("Vowels:", v_count)
print("Consonants:", c_count)