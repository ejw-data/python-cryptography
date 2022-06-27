# http://www.crypto-it.net/eng/simple/caesar-cipher.html
import getpass
import random
from time import sleep

def primeFromRange(x, y):
  '''
  Returns a randomly selected prime number from the range x,y
  Based on https://www.delftstack.com/howto/python/python-generate-prime-number/
  '''
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


def factor(x, limit):
    factors = []
    for n in range(2,limit,1):
        if (x % n == 0):
            factors.append(n)
    return factors


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


def phi_exp(phi_n):
    '''
    Find odd small number (3-29) that does not have a shared factor with phi_n
    '''
    e_list = []
    proposed_e = range(3,12,2)
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

def encrypt(text, KEY = 3):
  '''
  Function for encrypting text
  '''

  encrypted = ""
  for ch in text:
    if ord(ch) >= ord('a') and ord(ch) <= ord('z'):
      newCode = ord(ch) + (KEY % 26)
      if (newCode > ord('z')):
        newCode -= 26
      encrypted += chr(newCode)
    elif ord(ch) >= ord('A') and ord(ch) <= ord('Z'):
      newCode = ord(ch) + (KEY % 26)
      if (newCode > ord('Z')):
        newCode -= 26
      encrypted += chr(newCode)
    else:
      encrypted += " "
  return encrypted

def decrypt(text, KEY = 3):
  '''
  Function for decrypting text.
  '''

  decrypted = ""
  for ch in text:
    if ord(ch) >= ord('a') and ord(ch) <= ord('z'):
      newCode = ord(ch) - (KEY % 26)
      if (newCode < ord('a')):
        newCode += 26
      decrypted += chr(newCode)
    elif ord(ch) >= ord('A') and ord(ch) <= ord('Z'):
      newCode = ord(ch) - (KEY % 26)
      if (newCode < ord('A')):
        newCode += 26
      decrypted += chr(newCode)
    else:
      decrypted += " "
  return decrypted

def encrypted_messages():
  '''
  Used to send and receive encrypted messages.
  '''

  # Generate two prime numbers
  prime1 = primeFromRange(17, 40)
  prime2 = primeFromRange(17, 40)
  print(f"prime1,prime2: {(prime1, prime2)}")

  n_a = prime1*prime2

  phi_n_a = (prime1 - 1)*(prime2 - 1)

  ex_a = phi_exp(phi_n_a)
  print(f"ex: {ex_a}")

  # private key
  d_a = int((2*phi_n_a + 1)/ex_a)
  print(f"d: {d_a}")

  print(f"\nYour Public Key is:  {(ex_a,n_a)}")
  print(f"Your Private Key is hidden")

  
  ex_b = int(input("\nAsk the other person for their public key (e), Enter here: "))
  n_b = int(input("\nAsk the other person for their public key (n), Enter here: "))
 
  m_a_secret = int(input("\nYou should now enter a 4 digit secret number of your choosing, Enter here: "))
  
  #variable read crypted message from a using b keys
  cm_a_secret_b = m_a_secret**ex_b % n_b
  print(f"Your encreypted secret using the other persons public key is: {cm_a_secret_b}")
  print(f"Send this encrypted number to the other person as your secret for them to decode with their private key.")
  
  cm_b_secret_a = int(input("\nEnter the other persons secret that they created from your public keys, Enter here: "))

  m_b_secret = cm_b_secret_a**(d_a*ex_a) % n_a

  print(f"The secret from the other person decrypted with your private key is: {m_b_secret}")

  allowed_invalid_reponses = 3
  auto_exit = 0

  menu = 4
  while menu != 3:
      menu = int(input(f"\nWhat would you like to do now.  Select from these options:\n \
(1) Encrypt message\n \
(2) Decrypt message\n \
(3) End Program\n \
Enter only the number here:  "))

      if (menu == 1):
          message = input(f"\n Enter message here:\n ")
          encrypted = encrypt(message, KEY = cm_a_secret_b)
          print(f"\n Send this encrypted message to them:\n {encrypted}")
          auto_exit = 0
      elif (menu == 2):
          message = input(f"\n Enter the encrypted message here:\n ")
          decrypted = decrypt(message, KEY = m_b_secret)
          print(f"\n The decrypted message reads:\n {decrypted}")
          auto_exit = 0
      elif (menu ==3):
          print(f"\n Closing Program.  A new public key and key part will need to be shared next time.\n")
      else:
          auto_exit += 1
          if (auto_exit == allowed_invalid_reponses):
              print(f"{allowed_invalid_reponses} invalid responses.  Program exiting now.")
              menu = 3
          elif (auto_exit > 1):
              print(f"Warning:  Invalid Response.  Only enter 1,2,3.  You have {allowed_invalid_reponses - auto_exit} \
                tries left before program automatically closes.")
          else:
              print(f"I'm sorry but your response is unclear.  You can enter 1,2, or 3 only. Try again.")
        


def logic_test():
  '''
  Used for inputing different values to test the functionality of the code.
  '''
  key_public_a = 20
  key_private_a = 26
  key_public_b = 13
  key_private_b = 17

  allowed_invalid_reponses = 3
  auto_exit = 0
  continue_test = True

  while continue_test:

      print(f"\nThese are the values that have been entered:\n")
      print(f"Public Key A:  {key_public_a}")
      print(f"Private Key A:  {key_private_a}")
      print(f"Public Key B:  {key_public_b}")
      print(f"Private Key B:  {key_private_b}")

      key_part_a = (key_public_a**key_private_a) % key_public_b
      key_part_b = (key_public_a**key_private_b) % key_public_b

      print(f"Partial Key for A is {key_part_a} and Partial Key for B is {key_part_b}.")

      key_full_a = (key_part_b**key_private_a) % key_public_b
      key_full_b = (key_part_a**key_private_b) % key_public_b

      print(f"Full Key for A is {key_full_a} and Full Key for B is {key_full_b}.")

      menu = input(f"\nDo you want to enter your own values to test? (y/n): ")
      menu_valid = menu.upper()
      if (menu_valid == "Y" or menu_valid == "YES" or menu_valid == "1"):
          key_public_a = int(input(f"Submit a public key number ( <100 ) for person A:  "))
          key_private_a = int(input(f"Submit a private key number ( <100 ) for person A:  "))
          key_public_b = int(input(f"Submit a public key number ( <100 ) for person B:  "))
          key_private_b = int(input(f"Submit a private key number ( <100 ) for person B:  "))
          auto_exit = 0

      elif (menu_valid =="N" or menu_valid == "NO" or menu_valid == "0"):
          print(f"\nClosing program.\n")
          continue_test = False

      else:
        auto_exit += 1
        if (auto_exit == allowed_invalid_reponses):
            print(f"{allowed_invalid_reponses} invalid responses.  Program exiting now.")
            continue_test = False
        elif (auto_exit > 1):
            print(f"Warning:  Invalid Response.  Only enter 1,2,3.  You have {allowed_invalid_reponses - auto_exit} \
              tries left before program automatically closes.")
        else:
            print(f"I'm sorry but your response is unclear.  You can enter 'y' or 'n'. Try again.")




# Intial program
print(f"\n\nSelect which program to run:\n")
choice = int(input(f"(1) Add Person A and B Keys for Testing\n\
(2) Share Code with a Friend and Practice Sending Messages\n\
(3) End Program\n\
Enter Selection (1,2,3):  ") )

if (choice == 1):
  logic_test()
elif (choice == 2):
  encrypted_messages()
else:
  print("\nProgram Closing...\n")
