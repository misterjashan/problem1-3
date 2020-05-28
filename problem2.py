import itertools 

def isEvenOrOdd( L, R ): 
    oddCount = (R - L )/2
      
    if( R % 2 == 1 or L % 2 == 1): 
        oddCount = oddCount + 1
      
    if(oddCount % 2 == 0): 
        return "Even"
    else : 
        return "Odd"    
          
  
def testCases():
    firstRange = []
    secondRange = []
    result = []
    R = int() 
    L =  int()
    testcaseNo = int(input("Enter the number of testcases <<< "))
    for i in range(0, testcaseNo):
         R= int(input("Enter the range"))

         L = int(input("Enter the ending range"))
         firstRange.append(R)
         secondRange.append(L)
    for (L, R) in zip(secondRange, firstRange):
        results = isEvenOrOdd(L, R)
        result.append(results)
    print(firstRange)
    print(secondRange)    
    print(result)

         

    
         

          
# Driver Code 
  


  
print(testCases())