integer_n = int(input("\nEnter an integer: "))


#function to check if a given number is prime
def Prime_Checker(n):
  #since 0 and 1 is not prime return false.
    if(n==1 or n==0):  
        return False
   
  #Run a loop from 2 to n-1
    for i in range(2,n):
    #if the number is divisible by i, then n is not a prime number.
        if(n%i==0):
            return False
   
  #otherwise, n is prime number.
    return True
 
#check for every number and make a counter
count =0
num=2
#while the counter is not equal to the given integer
while count < integer_n: 
  #run the function checker
  if Prime_Checker(num):
    print(num, end=" ")
    #increment the counter
    count += 1
  #increment the current number to be checked
  num += 1

        