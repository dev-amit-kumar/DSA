def subString(Str,n): 
    for Len in range(1,n + 1):  
        for i in range(n - Len + 1):   
            j = i + Len - 1
            for k in range(i,j + 1): 
                print(Str[k],end="") 
            print() 
              
if __name__ == "__main__":          
    Str = input()
    subString(Str,len(Str)) 