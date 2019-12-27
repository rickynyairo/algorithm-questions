'''Solution to Q3 of the code challenge'''

def calculate(summation, xor): 
    A = (summation - xor)//2
    a, b = 0, 0
    for i in range(64): 
        Xi = (xor & (1 << i)) 
        Ai = (A & (1 << i)) 
        if (Xi == 0 and Ai == 0):  
            pass             
        elif (Xi == 0 and Ai > 0): 
            a = ((1 << i) | a)  
            b = ((1 << i) | b)         
        elif (Xi > 0 and Ai == 0): 
            a = ((1 << i) | a)  
  
        else: # (Xi == 1 and Ai == 1) 
            return -1
    return (min(a, b), max(a, b)) 

def main():
    # read N from stdin
    n: int = int(input())
    results = []
    for i in range(n):
        # confirm whether it is a note or a coin
        [summation, xor] = input().split()
        res = calculate(int(summation), int(xor))
        results.append(res)

    for res in results:
        try:
            print(res[0], res[1])
        except TypeError:
            print(res)

if __name__ == "__main__":
    main()
