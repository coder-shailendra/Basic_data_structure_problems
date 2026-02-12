def isPalindrome(s):
    cleaned = ""
    for ch in s:
        if ch.isalnum():      
            cleaned += ch.lower()
    return cleaned == cleaned[::-1]

print(isPalindrome("A man, a plan, a canal: Panama"))
print(isPalindrome("nitin"))
print(isPalindrome("my house is beautiful"))