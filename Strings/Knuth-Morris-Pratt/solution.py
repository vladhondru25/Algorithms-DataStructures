def lps(haystack, lps_array):
    i = 1
    j = 0

    while i < len(haystack):
        if haystack[i] == haystack[j]:
            j += 1
            lps_array[i] = j
            i += 1
        else:
            if j == 0:
                lps_array[i] = 0
                i += 1
            else:
                j = lps_array[j-1]


def kmp(haystack, needle):
    n = len(needle)
    h = len(haystack)
    if n > h:
        return -1
    
    lps_array = [0] * h
    lps(haystack,lps_array)

    i = 0
    j = 0
    while i < h:
        if haystack[i] == needle[j]:
            i += 1
            j += 1
        
        if j == n:
            # j = lps_array[j-1] # Use if more than the just the first occurance is required
            return i-n
        elif i<h and haystack[i] != needle[j]:
            if j == 0:
                i += 1
            else:
                i = lps_array[j-1]

    return -1

print("Matching pattern starting index is: " + str(kmp("hello","ll")))