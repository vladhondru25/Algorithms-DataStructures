import random

def shuffle(a):
    for i in range(len(a)):
        idx = random.randint(0,i)
        
        a[i], a[idx] = a[idx], a[i]
        
        
if __name__ == '__main__':
    array_to_shuffle = [0,1,2,3,4,5,6,7,8,9,10]
    
    shuffle(array_to_shuffle)
    
    print(f'Shuffled arrat: {array_to_shuffle}')
    