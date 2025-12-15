strings = ["apple", "banana", "grapes"]
char = "a"

count_list = []
total_count = 0

for s in strings:
    count = 0
    for ch in s:
        if ch == char:
            count += 1
    count_list.append(count)
    total_count += count

print("Counts per string:", count_list)
print("Total count:", total_count)
