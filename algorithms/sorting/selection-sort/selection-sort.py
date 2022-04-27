def sort(a):
    for i in range(len(a)):
        min_idx = i
        curr_no = a[i]
        
        for j in range(i,len(a)):
            if a[j] < curr_no:
                min_idx = j
                curr_no = a[j]
        
        a[i], a[min_idx] = a[min_idx], a[i]
        
        
if __name__ == '__main__':
    array_to_test = [4, 2, 7, 9, 1, 10, 5, 3, 8, 0, 6]
    
    sort(array_to_test)
    
    assert array_to_test == [0,1,2,3,4,5,6,7,8,9,10]
    
    print('Success!')