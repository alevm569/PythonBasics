from collections import Counter

def near_palindrome(s):
    freq = Counter(s)
    odd_count = sum(1 for count in freq.values() if count % 2 != 0)
    return max(0, odd_count - 1)

print("cocoa: ",near_palindrome("cocoa"))  
print("daddy: ", near_palindrome("daddy"))  
print("abcdefgh: ", near_palindrome("abcdefgh")) 
