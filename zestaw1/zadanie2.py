import sys

def get_arguments():
    argv = sys.argv[0:]
    numbers = []

    for i in range(1,len(argv)):
        numbers.append(int(sys.argv[i]))
    return numbers

def is_prime(n):
  for i in range(2,n):
    if (n%i) == 0:
      return False
  return True

arguments = get_arguments()

def calculation(arguments):
    powers = {}
    powers_all = []
    for num in arguments:
        dzielnik = 2
        licznik = 0
        while is_prime(int(num)) == False :
            while num % dzielnik == 0 :
                    num /= dzielnik
                    licznik += 1
            if(licznik != 0):
                powers[dzielnik] = licznik
            dzielnik += 1
            licznik = 0
        powers["prime"] = int(num) 
        powers_all.append(powers)
        powers = {}
    return powers_all    

def print_results(num_after_calculation):
    for d in num_after_calculation :
        result = ""
        for key in d:
            if(key == 'prime'):
                result += str(d[key])
            elif(d[key] == 1):
                result += str(key) + "*"    
            else:    
                result += str(key) + "^" + str(d[key]) + "*"
        index = num_after_calculation.index(d)        
        print(arguments[index]," = ", result)  
        
num_after_calculation = calculation(arguments)      
print_results(num_after_calculation)           