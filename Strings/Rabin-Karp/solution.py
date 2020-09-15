def rabin_karp(haystack, needle):
    n = len(needle)
    h = len(haystack)
    if n > h:
        return -1
    
    a = 26 # Polynomial base
    modulus = 2**31 # Modulus value to avoid overflow
    
    # Lambda-functions to convert character to integer
    h_to_int = lambda i : ord(haystack[i]) - ord('a')
    needle_to_int = lambda i : ord(needle[i]) - ord('a')
    
    # First compute hash of needle and the same length for haystack
    haystack_hash = 0
    needle_hash = 0
    for i in range(n):
        haystack_hash = (haystack_hash * a + h_to_int(i)) % modulus
        needle_hash = (needle_hash * a + needle_to_int(i)) % modulus
    if haystack_hash == needle_hash:
        return 0
    
    an = (a**n) % modulus # Term to be multiplied with the element that must be subtracted from rolling hash
    
    for start in range(1, h - n + 1):
        haystack_hash = (haystack_hash * a - h_to_int(start - 1) * an + h_to_int(start + n - 1)) % modulus
        if haystack_hash == needle_hash:
            return start

    return -1

print("Matching pattern starting index is: " + str(rabin_karp("hello","ll")))