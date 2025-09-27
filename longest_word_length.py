str= "python is easy and simple language"

words = str.split()               
max_len = max(len(word)  for word in words) 
print("Longest word length:", max_len)
