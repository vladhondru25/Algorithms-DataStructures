def sort(a):
    for i in range(len(a)):
        curr_no = a[i]
        
        for j in range(i,0,-1):
            if a[j-1] > curr_no:
                a[j-1], a[j] = a[j], a[j-1]
        
        
if __name__ == '__main__':
    array_to_test = [4, 2, 7, 9, 1, 10, 5, 3, 8, 0, 6]
    
    sort(array_to_test)
    
    assert array_to_test == [0,1,2,3,4,5,6,7,8,9,10]
    
    print('Success!')