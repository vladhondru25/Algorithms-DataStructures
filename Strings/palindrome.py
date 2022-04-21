def check_palindrome(ss):
    middle = len(ss) // 2
    
    first_part  = ss[0:middle]
    if len(ss) % 2 != 0:
        middle = middle + 1
    second_part = ss[middle:][::-1] # ss[-1:middle-1:-1]
    
    if first_part == second_part:
        return True
    else:
        return False
    
def check_palindrome2(ss):
    if ss == ss[::-1]:
        return True
    else:
        return False
    
    
if __name__ == "__main__":
    print(check_palindrome('suggus'))
    print(check_palindrome('sugus'))
    print()
    print(check_palindrome2('suggus'))
    print(check_palindrome2('sugus'))