import random 
from time import sleep

def primeFromRange(x, y):
    sleep(1)
    random_number = random.randrange(x,y,1)
    prime_range = 10

    for n in range(random_number, random_number+prime_range):
        
        for num in range(2, n):
            isPrime = True
            if n % num == 0:
                isPrime = False
                break 

        if isPrime:
            prime_number = n 
            break
            
    return prime_number
# print(primeFromRange(10,50))



def prime(val):
    isPrime = True
    for num in range(2, val):
        if val % num == 0:
            isPrime = False
    if isPrime:
        prime_number = True
    else:
        prime_number = False
    return prime_number
# print(prime(2))




def factor(x, limit):
    factors = []
    for n in range(2,limit,1):
        if (x % n == 0):
            factors.append(n)
    return factors
# print(factor(2000, 2000))



def primeFactorization(val):

    primeFactors = []
    factors = factor(val, val)

    if factors:
        for x in factors:
            if factor(x,x):
                continue
            else:
                if x not in primeFactors:
                    primeFactors.append(x)
    else:
        print("No Factors.  This is already a prime number")
        primeFactors = [1,val]
      
    return primeFactors
# print(primeFactorization(2310))




def phi_exp(phi_n):
    '''
    Find odd small number (3-29) that does not have a shared factor with phi_n
    '''
    e_list = []
    proposed_e = range(3,15,2)
    prime_factors_phi_n = primeFactorization(phi_n) 

    for i in proposed_e:
        if prime(i):
            if (i not in prime_factors_phi_n):
                e_list.append(i)

        else:
            prime_list = primeFactorization(i)
            for j in prime_list:
                if (j not in prime_factors_phi_n) & (j not in e_list):
                    e_list.append(j)
    
    random_index = random.randrange(0,len(e_list),1)
    return e_list[random_index]
# print(phi_exp(23*31))



def test_calc():
    cm_b_secret_a = 13944
    d_a = 20114
    n_a = 31274
    ex_a = 11
    
    m_b_secret = cm_b_secret_a**(d_a*ex_a) % n_a
    return m_b_secret
# print(test_calc())

def test2():
    prime1 = primeFromRange(15, 30)
    prime2 = primeFromRange(15, 30)
    n_a = prime1*prime2
    phi_n_a = (prime1 - 1)*(prime2 - 1)
    ex_a = phi_exp(phi_n_a)
    # private key
    d_a = int((phi_n_a + 1)/ex_a)
    print(f"\nYour Public Key is:  {(ex_a,n_a)}")
    print(f"Your Private Key is hidden")



    # prime3 = primeFromRange(15, 30)
    # prime4 = primeFromRange(15, 30)
    # n_b = prime3*prime4
    # phi_n_b = (prime3 - 1)*(prime4 - 1)
    # ex_b = phi_exp(phi_n_b)
    # # private key
    # d_b = (phi_n_b + 1)/ex_b
    # print(f"\nYour Public Key is:  {(ex_b,n_b)}")
    # print(f"Your Private Key is hidden")

    
    # m_a_secret = 11
    m_b_secret = 6
    
    #variable read crypted message from a using b keys
    # cm_a_secret_b = m_a_secret**ex_b % n_b
    # print(f"The encreypted secret is: {cm_a_secret_b}")
    # print(f"Send this number to Person B as your secret.")
    
    # variable reads crypted message from b using a keys
    cm_b_secret_a = m_b_secret**ex_a % n_a
    print(f"The encreypted secret is: {cm_b_secret_a}")
    print(f"Send this number to Person B as your secret.")
    print(f"1:  {cm_b_secret_a}")
    print(f"2:  {m_b_secret}")
    print(f"3:  {ex_a}")
    print(f"4:  {n_a}")
    # m_a_secret_dc = cm_a_secret_b**(d_b*ex_b) % n_b
    m_b_secret_dc = cm_b_secret_a**(d_a*ex_a) % n_a

    # print(f"The decrypted secret is: {m_a_secret_dc}")
    print(f"The decrypted secret is: {m_b_secret_dc}")
    print(f"The secret should be {m_b_secret}")
# print(test2())



def find_k():
    '''
    Find the K value of the RSA algorithm
    '''
    prime1 = primeFromRange(15, 30)
    prime2 = primeFromRange(15, 30)
    phi_n_a = (prime1 - 1)*(prime2 - 1)
    ex_a = phi_exp(phi_n_a)
    print(f"phi: {phi_n_a}")
    print(f"e: {ex_a}")
    
    a =[1,0]
    b = [0,1]
    d = [int(phi_n_a), ex_a] 
    k = [0, int(phi_n_a/ex_a)]

    j =10
    
    for i in range(2,j):
        print(f"Loop #{i}")
        if (d[i-1] != 1):
            d_new = d[i-2] - (d[i-1]*k[i-1])
            a.append(a[i-2] - (a[i-1]*k[i-1]))
            b.append(b[i-2] - (b[i-1]*k[i-1]))
            d.append(d_new)
            k.append(int(d[i-1]/d_new))
        else:
            j = i+1
            # or set to exit the loop
            print(f"d: {d[i-1]}")
            print(f"a: {a[i-1]}")
            print(f"b_: {b[i-1]}")
            print(f"k: {k[i-1]}")
        


    if (b[i-1] > phi_n_a):
        b[i-1] = b[i-1] % phi_n_a
    if (b[i-1] < 0):
        b[i-1] = int(b[i-1]) + int(phi_n_a)

    print(f"b_final is: {b[i-1]}")
    print(f"Last Iteration is: {i}")

# print(find_k())

def find_k2():
    '''
    Find the K value of the RSA algorithm
    '''
    prime1 = primeFromRange(15, 30)
    prime2 = primeFromRange(15, 30)
    print(f"Prime1: {prime1}")
    print(f"Prime2: {prime2}")
    phi_n_a = (prime1 - 1)*(prime2 - 1)
    ex_a = phi_exp(phi_n_a)
    print(f"phi: {phi_n_a}")
    print(f"e: {ex_a}")
    
    a =[1,0]
    b = [0,1]
    d = [int(phi_n_a), ex_a] 
    k = [0, int(phi_n_a/ex_a)]

    j =10
    
    for i in range(1,j):
        
        if (d[i] != 1):
            d_new = d[i-1] - (d[i]*k[i])
            a.append(a[i-1] - (a[i]*k[i]))
            b.append(b[i-1] - (b[i]*k[i]))
            d.append(d_new)
            k.append(int(d[i]/d_new))
            print(f"Loop #{i-1}")
            print(f"d: {d[i]}")
        else:
            # or set to exit the loop
            print(f"Loop #{i-1}")
            print(f"d: {d[i]}")
            print(f"a: {a[i]}")
            print(f"b_: {b[i]}")
            print(f"k: {k[i]}")

            break
        


    # if (b[i] > phi_n_a):
    #     b[i] = b[i] % phi_n_a
    # if (b[i] < 0):
    #     b[i] = int(b[i]) + int(phi_n_a)

    # print(f"b_final is: {b[i]}")

print(find_k2())