import sys



def rec( n1 , n2 , n3):
    
    if n1 > n2 and n1 > n3 :
        
        if n2>n3:
            return n2*2+n3
        else:
            return n3*2+n2
    
    
    elif n2 > n1 and n2 > n3:
        
        if n1>n3:
            return n1*2+n3 
        else:
            return n3*2+n1

        
    elif n3>n1 and n3>n2:
        
        if n1>n2:
            return n1*2+n2 
        else:
            return n2*2+n1

    else:
        return n1+n2+n3
        
    



def main():

    for line in sys.stdin:
        n = [int(x) for x in line.split()]  
        
        tt = rec(n[0], n[1] ,n[2])

        print (tt)


if __name__ == "__main__": 
    main() 



